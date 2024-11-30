import sys
from configparser import ConfigParser #use to load api key
from chatbot import ChatBot

def main():
    #load api key
    config = ConfigParser()
    config.read('credentials.ini')
    #api_key = config['gemini_ai']["API_KEY"]
    api_key = '' #put api key here, couldn't get config parser to work yet

    #create chatbot object
    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()
    # chatbot.clear_conversation()

    #preloaded intro message
    print("Welcome to a basic interview prep Gemini ChatBot. Type 'quit' to exit.")

    #
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            #print()
            sys.exit("Exiting ChatBot Session...")

        try :
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"Error: {e}")
main()
