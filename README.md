# Rudimentary Chatbot with Google Generative AI

This is a simple chatbot implementation powered by Google's Generative AI model. Follow the instructions below to set it up and run successfully.

## 🛠 Setup Instructions

1. **Clone the Repository**
   - Clone the project from the following GitHub repository from the terminal:
     ```bash
     git clone https://github.com/JoshChiaCPP/cs2520-final.git
     ```
   - Navigate into the project folder:
     ```bash
     cd cs2520-final
     ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
3. **Activate the virtual environment**
   ```bash
   source venv/bin/activate # For window: venv\Scripts\activate
4. **Install the required Python packages**
   ```bash
   pip install google-generativeai
3. **Set Up Your API Key**
   - Create a file named `credentials.ini` in the project folder.
   - Insert your API key in the required format inside the `credentials.ini` file.
     ```bash
     [gemini_ai]
     API_KEY = 
     ```
4. **Run the Chatbot**
   - Run the command:
     ```bash
     python app.py
     ```
   - If all required packages are installed and your `credentials.ini` file is set up correctly, the chatbot should start running.

## 📋 Prerequisites

- Python 3.9 or higher.
- The `google-generativeai` package installed:
  ```bash
  pip install google-generativeai
- Visual Studio Code (Recommended)
