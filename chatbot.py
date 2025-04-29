def get_bot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great!"
    elif "your name" in user_input:
        return "I'm ChatBot, your friendly assistant."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm not sure how to respond to that."

def chat():
    print("Welcome to ChatBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! 👋")
            break
        response = get_bot_response(user_input)
        print("ChatBot:", response)

# Run the chatbot
chat()
