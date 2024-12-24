def chatbot():
    print("Hello! I am a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        elif "hello" in user_input.lower():
            print("Chatbot: Hi there! How can I help you?")
        
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm just a program, but thanks for asking!")
        
        elif "your name" in user_input.lower():
            print("Chatbot: I am a simple chatbot created in Python.")
        
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

# Run the chatbot
chatbot()
