import requests
from PIL import Image
from io import BytesIO
import pwinput
import os


def generate_image(prompt, api_key, output_format, custom_name):
    print("Generating image, please wait...")

    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/core",
        headers={
            "authorization": f"Bearer {api_key}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": output_format,
        },
    )

    if response.status_code == 200:
        file_name = custom_name if custom_name else prompt
        file_name = "".join(
            c for c in file_name if c.isalnum() or c in (' ', '_', '-'))
        image_path = f"./{file_name}.{output_format}"

        counter = 1
        while os.path.exists(image_path):
            image_path = f"./{file_name}_{counter}.{output_format}"
            counter += 1

        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"Image generated successfully and saved as {image_path}")

        image = Image.open(BytesIO(response.content))
        image.show()
        return image_path
    elif response.status_code == 401:
        raise Exception("API key is invalid or expired")
    else:
        raise Exception(str(response.json()))


def get_api_key():
    return pwinput.pwinput(prompt="Enter your API key: ")


def main():
    while True:
        prompt = input("Enter your prompt: ")
        api_key = get_api_key()

        custom_name = input(
            "Enter a custom name for the image (or press Enter to skip): ")

        while True:
            output_format = input(
                "Enter the output format (jpeg/png/webp): ").lower()
            if output_format in ['jpeg', 'png', 'webp']:
                break
            print("Invalid format. Please choose jpeg, png, or webp.")

        print("Processing your request...")

        try:
            generate_image(prompt, api_key, output_format, custom_name)
        except Exception as e:
            print(f"Error: {e}")

        choice = input(
            "Do you want to generate another image? (yes/no): ").lower()
        if choice not in ['yes', 'y']:
            print("Thank you for using the image generator. Goodbye!")
            break


if __name__ == "__main__":
    main()
