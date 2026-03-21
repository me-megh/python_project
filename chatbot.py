
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": "Hi! How can I assist you today?"
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you later"],
        "response": "Goodbye! Have a great day!"
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thanks a lot"],
        "response": "You're welcome! Glad I could help."
    }
}

def process_text(text):
    token=word_tokenize(text.lower())
    return token
def match_intent(user_input):
    user_token=process_text(user_input)
    for intent,data in intents.items():
        for pattern in data['patterns']:
            token_pattern=process_text(pattern)
            if any(token in user_token for token in token_pattern):
                return data['response']
    return "Sorry, I didn’t understand that." 
def chatbot():
    print("Chatbot: Hi,I'm here to help you. Type 'bye' to exit ")
    while True:
        user_input=input("You: ")
        if user_input.lower() in ['bie','bye','goodbye']:
            print("Chatbot: Good Bye")
            break
        response=match_intent(user_input)
        print(response)
chatbot()