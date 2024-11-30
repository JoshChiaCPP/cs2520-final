import sys
from configparser import ConfigParser
from chatbot import ChatBot

def main():
    # Load API key
    config = ConfigParser()
    config.read('credentials.ini')
    
    # Check for API key is in credentials.ini
    if 'gemini_ai' not in config:
        sys.exit("Error: Section 'gemini_ai' not found in 'credentials.ini'.")
    if 'API_KEY' not in config['gemini_ai']:
        sys.exit("Error: 'API_KEY' not found under 'gemini_ai' section in 'credentials.ini'.")

    # Get API key
    api_key = config['gemini_ai']['API_KEY']
    
    # Check for API key is not empty
    if not api_key:
        sys.exit("Error: API_KEY is empty in 'credentials.ini'.")

    # Create chatbot object
    chatbot = ChatBot(api_key=api_key)
    
    # Preloaded intro message
    print("Welcome to the Gemini AI Interview Prep ChatBot. Type 'quit' to exit.")

    # Start conversation
    while True:
        user_input = input("You: ")
        # Check if user wants to quit
        if user_input.lower() == "quit":
            sys.exit("Exiting ChatBot Session...")

        # Send prompt
        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
