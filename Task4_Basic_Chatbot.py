"""
CodeAlpha - Python Programming Task 4
Project: Basic Rule-Based Chatbot

Description:
A simple console chatbot that responds to predefined user messages.
"""

def chatbot():
    print("=" * 45)
    print("          BASIC CHATBOT - CODEALPHA")
    print("=" * 45)
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ("hello", "hi", "hey"):
            print("Bot: Hi! How can I help you?")

        elif user_input in ("how are you", "how are you?"):
            print("Bot: I'm fine, thanks! How are you?")

        elif user_input in ("what is your name", "what is your name?"):
            print("Bot: I'm a simple Python rule-based chatbot.")

        elif user_input in ("help", "what can you do"):
            print("Bot: I can respond to simple greetings and questions.")

        elif user_input in ("bye", "goodbye", "exit"):
            print("Bot: Goodbye! Have a great day!")
            break

        elif user_input == "":
            print("Bot: Please type something.")

        else:
            print("Bot: Sorry, I don't understand that yet.")


if __name__ == "__main__":
    chatbot()
