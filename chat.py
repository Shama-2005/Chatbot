import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    (r'hi|hello|hey',
     ['Hello!', 'Hi there!', 'Hey!']),
    (r'help',
     ['How can I assist you?', 'What do you need help with?']),
    (r'bye|goodbye',
     ['Goodbye!', 'Bye!', 'Have a nice day!']),
    (r'my name is Abdulla',
     ['Hello %1! How can I help you today?']),
    (r'(.*) (location|city) ?',
     ['We are located in XYZ city.']),
    (r'(.*)',
     ['Sorry, I didn\'t understand that. Can you please rephrase?'])
]
def chatbot():
    print("Welcome! How can I help you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("Bot:", response)
        if user_input.lower() == 'exit':
            break
if __name__ == "__main__":
    nltk.download('punkt')  # Ensure NLTK resources are downloaded
    chatbot()
