# Task 1: Rule-Based Chatbot - CodSoft Internship

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm a simple AI chatbot created for CodSoft Internship!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day 🙂"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! How about you?"
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

# Chat loop
print("Chatbot: Hi, I’m your assistant. Type 'bye' to end.")
while True:
    user = input("You: ")
    if "bye" in user.lower():
        print("Chatbot: Goodbye! Take care.")
        break
    response = chatbot_response(user)
    print("Chatbot:", response)
