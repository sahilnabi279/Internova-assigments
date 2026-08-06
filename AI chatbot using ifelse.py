print("Welcome to AI Chatbot")
print("Type 'bye' to exit the chatbot.")

while True:

    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hello! Welcome.")

    elif user == "hi":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm fine. Thank you for asking!")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language used in AI.")

    elif user == "who created you":
        print("Bot: I am a simple rule-based chatbot created using Python.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")