import json
import random

class BeautyInstructorChatbot:
    def __init__(self, dataset_path):
        with open(dataset_path, "r") as file:
            self.dataset = json.load(file)["intents"]

    def get_response(self, user_input):
        for intent in self.dataset:
            for pattern in intent["patterns"]:
                if pattern.lower() in user_input.lower():
                    return random.choice(intent["responses"])
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

if __name__ == "__main__":
    dataset_path = "../data/Beauty_instructor.json"
    chatbot = BeautyInstructorChatbot(dataset_path)

    print("Chatbot: Hello! I'm here to provide beauty tips and advice. How can I assist you today?")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! If you have more questions, feel free to ask.")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)