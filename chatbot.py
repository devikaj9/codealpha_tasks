
def chatbot():
    print("================================")
    print("       Welcome to ChatBot       ")
    print("================================")
    print("Type 'hello', 'how are you', 'give me motivational quote', or 'bye'.")
    print()

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("ChatBot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("ChatBot: I'm fine, thanks! How are you?")

        elif user_input == "give me motivational quote":
            print("ChatBot:It always seems impossible until it's done.")


        elif user_input == "what can you do":
            print("ChatBot: I can have a simple conversation with you.")

        elif user_input == "thank you" or user_input == "thanks":
            print("ChatBot: You're welcome!")

        elif user_input == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break

        else:
            print("ChatBot: Sorry, I don't understand that.")



chatbot()