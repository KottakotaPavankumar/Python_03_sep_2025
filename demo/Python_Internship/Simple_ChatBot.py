# Filename: simple_chatbot.py

import random
import re


def chatbot():
    """Simple rule-based chatbot with predefined responses"""

    # Predefined responses dictionary
    responses = {
        'greeting': [
            "Hi there! How can I help you?",
            "Hello! Nice to meet you!",
            "Hey! What's up?",
            "Hi! How are you doing today?"
        ],
        'how_are_you': [
            "I'm fine, thanks! How about you?",
            "I'm doing great! Thanks for asking!",
            "I'm just a program, but I'm functioning well!",
            "Feeling good! What about you?"
        ],
        'goodbye': [
            "Goodbye! Have a great day!",
            "Bye! See you later!",
            "Take care! Come back soon!",
            "Farewell! It was nice talking to you!"
        ],
        'thanks': [
            "You're welcome!",
            "No problem! Happy to help!",
            "Anytime! Glad I could assist!",
            "My pleasure!"
        ],
        'name': [
            "I'm a simple chatbot created with Python!",
            "You can call me PyBot!",
            "I'm your friendly Python assistant!",
            "I'm a chatbot here to help you!"
        ],
        'help': [
            "I can respond to greetings, questions about how I am, and goodbyes!",
            "Try saying: hello, how are you, what's your name, or bye!",
            "I'm here to chat! Ask me anything simple!",
            "Just talk to me! I understand basic conversations."
        ],
        'age': [
            "I was just created, so I'm brand new!",
            "Age is just a number for a bot like me!",
            "I'm timeless in the digital world!",
            "I don't age, I just get updated!"
        ],
        'default': [
            "I'm not sure I understand. Can you rephrase?",
            "Hmm, I don't quite get that. Try something else!",
            "Sorry, I didn't catch that. Could you say it differently?",
            "I'm still learning! Try asking something simpler."
        ]
    }

    # Patterns for matching user input
    patterns = {
        'greeting': r'\b(hello|hi|hey|greetings|good morning|good evening|good afternoon)\b',
        'how_are_you': r'\b(how are you|how\'s it going|how do you do|what\'s up|how are things)\b',
        'goodbye': r'\b(bye|goodbye|see you|farewell|exit|quit|later)\b',
        'thanks': r'\b(thanks|thank you|thx|appreciate|grateful)\b',
        'name': r'\b(your name|who are you|what are you called|what\'s your name)\b',
        'help': r'\b(help|assist|support|what can you do)\b',
        'age': r'\b(your age|how old|age)\b'
    }

    print("=" * 60)
    print("            WELCOME TO SIMPLE CHATBOT")
    print("=" * 60)
    print("Hi! I'm a simple chatbot. Type 'bye' or 'exit' to quit.")
    print("=" * 60 + "\n")

    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check if input is empty
        if not user_input:
            print("Bot: Please say something!\n")
            continue

        # Convert to lowercase for matching
        user_input_lower = user_input.lower()

        # Check for exit condition
        if re.search(patterns['goodbye'], user_input_lower):
            print(f"Bot: {random.choice(responses['goodbye'])}\n")
            break

        # Match user input with patterns
        response_found = False

        for intent, pattern in patterns.items():
            if re.search(pattern, user_input_lower):
                print(f"Bot: {random.choice(responses[intent])}\n")
                response_found = True
                break

        # Default response if no pattern matched
        if not response_found:
            print(f"Bot: {random.choice(responses['default'])}\n")


def main():
    """Main function to run the chatbot"""
    try:
        chatbot()
    except KeyboardInterrupt:
        print("\n\nBot: Interrupted! Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
