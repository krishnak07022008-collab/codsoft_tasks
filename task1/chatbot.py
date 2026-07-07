def chatbot():
    print("🤖 ChatBot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hello! How can I help you?")

        elif "how are you" in user:
            print("Bot: I'm doing great! Thanks for asking.")

        elif "your name" in user:
            print("Bot: I'm a Rule-Based ChatBot.")

        elif "help" in user:
            print("Bot: I can answer simple questions like greetings, my name, and the time.")

        elif "time" in user:
            from datetime import datetime
            print("Bot:", datetime.now().strftime("%I:%M %p"))

        elif "thank" in user:
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
