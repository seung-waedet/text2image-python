# text2image-python

Python Script for text2image generation with Stability AI

# Project Setup and API Connection Tutorial

This tutorial provides step-by-step instructions on how to set up a virtual environment for a Python project and how to connect to an API using the `requests` library.

## Setting Up a Virtual Environment

Using a virtual environment ensures that your project dependencies are isolated and prevents conflicts with other projects.

### Step-by-Step Instructions

1. **Install Virtualenv (if not already installed):**

   ```bash
   pip install virtualenv
   ```

2. **Navigate to Your Project Directory:**

   ```bash
   cd /path/to/your/project
   ```

3. **Create a Virtual Environment:**

   ```bash
   virtualenv venv
   ```

   This command creates a directory named `venv` in your project directory.

4. **Activate the Virtual Environment:**

   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install Required Packages:**
   Once the virtual environment is activated, you can install any required packages using pip. For example:
   ```bash
   pip install requests
   ```
