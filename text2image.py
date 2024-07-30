import requests
from PIL import Image
from io import BytesIO
import pwinput


def generate_image(prompt, api_key):
    # Display progress message
    print("Generating image, please wait...")

    # Make the API request
    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/core",
        headers={
            "authorization": f"Bearer {api_key}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": "jpeg",
        },
    )

    # Check the response status code
    if response.status_code == 200:
        # Save the image to a file
        image_path = f"./{prompt}.jpeg"
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print("Image generated successfully")

        # Display the image from the terminal
        image = Image.open(BytesIO(response.content))
        image.show()
        return image_path
    else:
        raise Exception(str(response.json()))


# Get user input for prompt and API key
prompt = input("Enter your prompt: ")
api_key = pwinput.pwinput(prompt="Enter your API key: ")

# Show progress message after getting input
print("Processing your request...")

# Generate and display the image
generate_image(prompt, api_key)
