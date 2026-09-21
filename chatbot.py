# CodeOrbit Tech - Rule-Based Chatbot
# Task 1: Artificial Intelligence Internship

print("🤖 Welcome to Kaviya's AI Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    # Handle greetings
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    # Handle name question
    elif "your name" in user_input:
        print("Bot: My name is Kaviya's AI Chatbot.")

    # Handle how are you question
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thank you for asking.")

    # Handle help request
    elif "help" in user_input:
        print("Bot: I can answer simple questions and greetings.")

    # Exit the chatbot
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    # Fallback response for unknown input
    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")