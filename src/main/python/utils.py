import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import io
import requests
import time
import json
import urllib.parse
import random

# Load environment variables from the .env file in the root directory
load_dotenv()

# Configure the Google API key
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Error: GEMINI_API_KEY is not set in the .env file.")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(e)

# --- GEMINI MODELS CONFIGURATION ---
# Models list synchronized with app.py to ensure consistency.
# If the primary model fails (404/429), the code will try the next ones.
GEMINI_MODELS_TO_TRY = [
    'gemini-2.5-flash',     # Primary: Best performance
    'gemini-1.5-flash',     # Fallback 1: High rate limits
    'gemini-1.5-flash-001', # Fallback 2: Specific version
    'gemini-1.5-pro'        # Fallback 3: Advanced reasoning
]

def get_image_description(image_file_storage, prompt_text):
    """
    Generates a description for a given image using Gemini models with robust fallback.
    It iterates through GEMINI_MODELS_TO_TRY until a successful response is received.
    """
    try:
        # Prepare the image
        image_bytes = image_file_storage.read()
        img = Image.open(io.BytesIO(image_bytes))
        
        last_error = None
        
        # Loop through models to find one that works
        for model_name in GEMINI_MODELS_TO_TRY:
            try:
                print(f"[DEBUG] Attempting Image Description with Model: {model_name}")
                model = genai.GenerativeModel(model_name)
                
                # Generate content
                response = model.generate_content([prompt_text, img])
                
                # If successful, return text immediately
                return response.text
                
            except Exception as e:
                error_str = str(e).lower()
                print(f"[DEBUG] Model {model_name} failed: {error_str}")
                
                # If Quota error (429) or Not Found (404), wait briefly and continue
                if "429" in error_str or "quota" in error_str or "404" in error_str or "not found" in error_str:
                    time.sleep(1)
                
                last_error = e
                continue # Try the next model
        
        # If all models fail, raise the last error to be caught below
        if last_error:
            raise last_error
        else:
            raise Exception("All models failed without specific error.")

    except Exception as e:
        error_message = str(e).lower()
        print(f"CRITICAL Error generating image description: {e}")

        if "quota" in error_message:
            return "I'm currently experiencing a high volume of requests. Please try again in a little while."
        elif "404" in error_message or "not found" in error_message:
            return "The AI vision service is currently unavailable. Please check the API configuration."
        else:
            return "I seem to be having some technical difficulties describing the image. Please ensure the file is a valid image and try again later."

# --- POLLINATIONS.AI FALLBACK FUNCTION ---
def generate_with_pollinations(prompt):
    """
    Generates an image using Pollinations.ai (Free, No Key required).
    This serves as a robust fallback when Hugging Face fails.
    """
    try:
        print(f"[DEBUG] Attempting fallback to Pollinations.ai for prompt: {prompt[:30]}...")
        encoded_prompt = urllib.parse.quote(prompt)
        # Random seed to ensure different images for same prompt
        seed = random.randint(0, 100000)
        
        # Pollinations URL (High Quality settings)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?seed={seed}&nologo=true&width=1024&height=1024"
        
        response = requests.get(url, timeout=35)
        
        if response.status_code == 200:
            print("[DEBUG] Success with Pollinations.ai")
            return response.content
        else:
            print(f"[DEBUG] Pollinations.ai failed with status: {response.status_code}")
            return None
    except Exception as e:
        print(f"[DEBUG] Error with Pollinations.ai: {e}")
        return None

# --- MAIN IMAGE GENERATION FUNCTION ---
def generate_image_from_prompt(prompt: str):
    """
    Hybrid Image Generation:
    1. Try Hugging Face API with updated Free-Tier friendly models.
    2. Fallback to Pollinations.ai if HF fails (404/410/Auth Error).
    """
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    
    # 1. Hugging Face Logic (Only if Key exists)
    if api_key:
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {"inputs": prompt}
        
        # Updated Model List: Prioritizing models that often work on Free Tier
        # 'router' URL is strictly used as 'api-inference' is deprecated.
        models_to_try = [
            "stabilityai/stable-diffusion-3.5-large", # Newest, often promoted
            "stabilityai/stable-diffusion-3.5-large-turbo",
            "runwayml/stable-diffusion-v1-5",         # Old faithful
            "black-forest-labs/FLUX.1-schnell"        # High quality (might be gated)
        ]

        for model_id in models_to_try:
            # Using the new ROUTER endpoint as required by HF
            api_url = f"https://router.huggingface.co/models/{model_id}"
            print(f"[DEBUG] Trying HF Model: {model_id}")
            
            try:
                response = requests.post(api_url, headers=headers, json=payload, timeout=25)
                
                # Success
                if response.status_code == 200 and response.headers.get("content-type", "").startswith("image/"):
                    print(f"[DEBUG] Success with Hugging Face: {model_id}")
                    return response.content
                
                # Model Loading (503) -> Skip to be faster, let Pollinations handle it
                elif response.status_code == 503:
                    print(f"[DEBUG] Model {model_id} is loading (503). Skipping to next/fallback for speed.")
                    continue
                
                # Fatal Errors (404 Not Found / 410 Gone / 401 Auth)
                elif response.status_code in [400, 401, 403, 404, 410]:
                    try:
                        # Try to read error text
                        err_text = response.json().get("error", "Unknown")
                    except:
                        err_text = "Unknown Error"
                    print(f"[DEBUG] HF Error {response.status_code} for {model_id}: {err_text}")
                    continue
                
                else:
                    print(f"[DEBUG] HF Unknown Error {response.status_code}")
            
            except Exception as e:
                print(f"[DEBUG] Connection Error for {model_id}: {e}")
                continue

    # 2. Fallback to Pollinations.ai (Guaranteed to work if internet is available)
    print("[DEBUG] All HF models failed or Key missing. Switching to Pollinations.ai Fallback...")
    image_data = generate_with_pollinations(prompt)
    
    if image_data:
        return image_data
    
    return "Unable to generate image. Please check your internet connection."