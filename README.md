# Rudimentary Chatbot with Google Generative AI

This is a simple chatbot implementation powered by Google's Generative AI model. Follow the instructions below to set it up and run successfully.

## 🛠 Setup Instructions

1. **Clone the Repository**
   - Clone the project from the following GitHub repository:
     ```bash
     git clone https://github.com/JoshChiaCPP/cs2520-final.git
     ```
   - Navigate into the project folder:
     ```bash
     cd cs2520-final
     ```

2. **Prepare Your Environment**
   - Ensure `app.py` and `chatbot.py` are in the same folder.
   - Confirm your Python environment has the `google-generativeai` package installed.

3. **Set Up Your API Key**
   - Create a file named `credentials.ini` in the project folder.
   - Insert your API key in the required format inside the `credentials.ini` file.
     ```bash
     [gemini_ai]
     API_KEY = 
     ```

4. **Run the Chatbot**
   - Open a terminal in the project folder, or navigate there using `cd` in your terminal.
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
