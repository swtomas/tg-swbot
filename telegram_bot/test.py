import requests
import urllib.parse

prompt = "A beautiful sunset over the ocean"
params = {
    "width": 1280,
    "height": 720,
    "seed": 42,
    "model": "flux",
    "nologo": "true", 
    "image": "https://example.com/input-image.jpg", # Optional - for image-to-image generation (kontext & gptimage)
    # "referrer": "MyPythonApp" # Optional for referrer-based authentication
}
encoded_prompt = urllib.parse.quote(prompt)
url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

try:
    response = requests.get(url, params=params, timeout=300) # Increased timeout for image generation
    response.raise_for_status() # Raise an exception for bad status codes

    with open('generated_image.jpg', 'wb') as f:
        f.write(response.content)
    print("Image saved as generated_image.jpg")

except requests.exceptions.RequestException as e:
    print(f"Error fetching image: {e}")
    # Consider checking response.text for error messages from the API
    # if response is not None: print(response.text)