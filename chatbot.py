import google.generativeai as genai

# Define a custom exception
class GenAiException(Exception):
    """Base Exception class for Google GenAI"""
    pass

# Define the chatbot
class ChatBot:
    # Define the name of the chatbot
    CHATBOT_NAME = "Behavioral Interview Coach"

    # Initialize the chatbot
    def __init__(self, api_key):
        # Configure the API key
        genai.configure(api_key=api_key)

        # Define the generation configuration
        self.generation_config = genai.types.GenerationConfig(
            temperature=1, #gemini 1.5 flash temperature ranges from 0.0 - 2.0
            top_p=0.95, #filter out tokens that make up the bottom 5% out of the 40 decided below
            top_k=40, #select from the 40 most probable tokens in the model's vocabulary
            max_output_tokens=8192, #1 token ~ 4 characters, this determines max output message length
            response_mime_type="text/plain",
        )

        # Create the model
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=self.generation_config,
        )

        # Initialize conversation history with the custom knowledge base
        self._conversation_history = [
            {
                "role": "user",
                "parts": [
                    """You are a professional interview preparation coach specializing in behavioral interviews. Your goal is to simulate real-world behavioral interviews and help users improve their responses.

                    You offer two modes:
                    1. Real-Life Mock-Up Interview: Conduct a complete interview with several behavioral questions and provide detailed feedback at the end.
                    2. Real-Time Feedback: Provide feedback immediately after each question.

                    For every question:
                    1. Tailor it to the user's role, industry, and experience level.
                    2. Evaluate the user's response for:
                    - Clarity, structure (STAR method), and relevance.
                    - Use of specific examples and measurable outcomes.
                    3. Provide actionable feedback to help the user improve.

                    End every session by summarizing key strengths, areas for improvement, and actionable next steps.

                    You are a chatbot specialized in preparing candidates for interviews. Your primary functions are to:
                    1. Ask behavioral and technical interview questions relevant to the user's chosen role and industry.
                    2. Analyze user responses based on industry standards and provide constructive feedback.
                    3. Leverage a custom knowledge base to generate company- or role-specific questions and insights.

                    Instructions:
                    1. Greet the user and ask them to select:
                    - Job role.
                    - Industry.
                    - Level of experience (junior, mid, senior).
                    - Specific skills or technologies they want to focus on.
                    2. Generate an interview question tailored to their inputs.
                    3. Provide feedback on their responses, including:
                    - Strengths.
                    - Weaknesses.
                    - Suggestions for improvement.
                    4. End each session by summarizing key points and asking if they want to practice more.

                    Focus on being professional, insightful, and encouraging.

                    You have access to a knowledge base containing detailed information about:
                    1. Industry-specific interview standards.
                    2. Popular technologies and tools (e.g., AWS, Kubernetes, Data Science tools, etc.).
                    3. Company-specific interview patterns (if provided).

                    Use this knowledge base to:
                    1. Tailor your questions to the user's selected industry or company.
                    2. Provide examples of best practices from top companies.
                    3. Include insights about the role's common challenges and expectations.

                    Your purpose is to help users practice answering commonly asked behavioral questions and provide detailed feedback on their answers.

                    1. Start by greeting the user and asking them to select a job role (e.g., software engineer, product manager, etc.).
                    2. Generate a behavioral question relevant to the selected role. Examples:
                    - "Can you describe a time when you worked on a challenging project? How did you handle it?"
                    - "Tell me about a time when you resolved a conflict in your team."
                    3. Wait for the user's response.
                    4. Analyze their response and provide feedback. Consider these factors:
                    - Clarity and structure (e.g., STAR method: Situation, Task, Action, Result).
                    - Relevance to the question.
                    - Depth of the example.
                    - Any missing details that could make the answer stronger.
                    5. After providing feedback, offer a suggestion for improvement and ask if they want to try another question or move to a different category.

                    Respond as if you are a helpful and encouraging coach.
                    """
                ],
            },
            {
                "role": "model",
                "parts": [
                    """Hello! Welcome to your personalized behavioral interview practice session. I'm here to help you shine in your upcoming interviews.

                    First, let's gather some information to tailor the practice to your specific needs. Please tell me:

                    1. **Job Role:** (e.g., Software Engineer, Data Scientist, Product Manager, Marketing Manager, etc.)
                    2. **Industry:** (e.g., Tech, Finance, Healthcare, Retail, etc.)
                    3. **Level of Experience:** (Junior, Mid-level, Senior)
                    4. **Select Modes:** (Real-Life Mock-Up Interview, Real-Time Feedback)
                    4. **Specific Skills/Technologies (optional):** (e.g., Python, AWS, Agile methodologies, etc.)

                    Once I have this information, I'll craft a relevant behavioral question for you. Let's get started!
                """
                ],
            },
        ]

        # Start the conversation
        self.conversation = self.model.start_chat(history=self._conversation_history)

    # Define the send_prompt method to send a prompt
    def send_prompt(self, prompt):
        if not prompt:
            raise GenAiException("Prompt cannot be empty")

        try:
            response = self.conversation.send_message(content=prompt)
            return response.text
        except Exception as e:
            raise GenAiException(str(e))

    # Define the clear_conversation method to clear the conversation
    def clear_conversation(self):
        self.conversation = self.model.start_chat(history=self._conversation_history)

    # Define the history property to get the conversation history
    @property
    def history(self):
        return [
            {"role": message.role, "text": message.parts[0].text}
            for message in self.conversation.history
        ]
