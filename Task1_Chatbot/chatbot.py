from utils import get_response

print("Chatbot 🤖: Hi, I’m your assistant. Type 'bye' to end.")
while True:
    user = input("You: ")
    response = get_response(user)
    print("Chatbot:", response)
    if "bye" in user.lower():
        break
