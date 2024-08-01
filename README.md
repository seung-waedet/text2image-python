# Text2Image

**Text2Image** is a user-friendly text-to-image generator that uses Stability AI's API to create images from text prompts. This Python script allows users to generate images in various formats (JPEG, PNG, WEBP) and save them with custom names.

## Features

- Generate images from text prompts using Stability AI's API.
- Supports multiple output formats: JPEG, PNG, WEBP.
- Custom naming for generated images.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `PIL` (Pillow), `pwinput`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/seung-waedet/text2image-python
   cd text2image


## Setting Up a Virtual Environment

Using a virtual environment ensures that your project dependencies are isolated and prevents conflicts with other projects.

### Step-by-Step Instructions

2. **Install Virtualenv (if not already installed):**

   ```bash
   pip install virtualenv
   ```

3. **Navigate to Your Project Directory:**

   ```bash
   cd /path/to/your/project
   ```

4. **Create a Virtual Environment:**

   ```bash
   virtualenv venv
   ```

   This command creates a directory named `venv` in your project directory.

5. **Activate the Virtual Environment:**

   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

6. **Install Required Packages:**
   Once the virtual environment is activated, you can install any required packages using pip. 

   ```bash
   pip install requests pillow pwinput
   ```
7. **Run the script:**

```bash
python text2image.py   
```
Follow the on-screen prompts:

- Enter your text prompt.
- Enter your Stability AI API key (if you don't have one, sign up and get it from Stability AI).
- Optionally, enter a custom name for the image.
- Choose the output format (JPEG, PNG, WEBP).
- The script will generate the image and display it. You can choose to generate another image or exit the application.

## Example
```
*** Welcome to Text2Image, Your user-friendly text generator ***

Please watch the video on our website to get familiar with creating images with this application.

Head over to https://platform.stability.ai/account/keys to sign up and grab your API Keys.

Enter your prompt: A beautiful sunset over the mountains
Enter your API key: ********************
Enter a custom name for the image (or press Enter to skip): sunset_mountains
Enter the output format (jpeg/png/webp): jpeg
Processing your request...
Generating image, please wait...
Image generated successfully and saved as ./sunset_mountains.jpeg
Do you want to generate another image? (yes/no): no
Thank you for using the image generator. Goodbye!
```





