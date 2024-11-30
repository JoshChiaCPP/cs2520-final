import google.generativeai as genai

#inhereit exception class
class GenAiException(Exception):
    """Base Exception class for Google GenAI"""

class ChatBot:
    """Simple ChatBot class that only implements google generative ai. This ChatBot currently has no external training data and only
    serves as a proof of being able to implement google generative ai methods. ChatBot may be limited in usage due to free API key
    limitations."""
    CHATBOT_NAME = "Gemini AI for interview prep"

    def __init__(self, api_key):
        self.genai = genai #create instance of genai object
        self.genai.configure(api_key=api_key) #attach api key
        self.model = self.genai.GenerativeModel("gemini-pro") #attach generative model object to chatbot, switch to 'gemini-flash-8b when using actual interview prep key
        self.conversation = None #conversation log
        self._conversation_history = [] #can preload context here to help the chatbot get a sense of direction for the conversation

        self.preload_conversation()

    def send_prompt(self, prompt, temp = 0.2):
        if temp < 0 or temp > 1 :
            raise GenAiException("Temperature must be between 0 and 1")
        if not prompt:
            raise GenAiException("Prompt cannot be empty")

        try:
            response = self.conversation.send_message(
                content=prompt,
                generation_config=self._generative_config(temp),
            )
            response.resolve() #if response has multiple parts, we get them all first
            return f"{response.text}\n" + "---" * 20 #to send together here
        except Exception as e:
            raise GenAiException(e.message)

    @property #property object comes with getter setter and deleter methods
    def history(self):
        conversation_history = [
            {"role" : message.role, "text" : message.parts[0].text} for message in self.conversation.history #reference history attribute in conversation object
        ]
        return conversation_history

    def clear_conversation(self):
        self.conversation = self.model.start_chat(history=[])

    def start_conversation(self):
        self.conversation = self.model.start_chat(history=self._conversation_history)

    def _generative_config(self, temp):
        return genai.types.GenerationConfig(
            #candidate_count=1, is already the default, so 1 output at a time
            temperature=temp #temperature determines how 'creative' the response is, value between 0-1, where 1 is creative. Reccomended to set low for interview prep
        )

    def _construct_message(self, text, role="user"):
        return {
            #role = user or ai
            "role": role,
            "parts": [text] #make sure it's in a list
        }
    def preload_conversation(self, conversation_history=None):
        if isinstance(conversation_history, list) :
            self._conversation_history = conversation_history


    