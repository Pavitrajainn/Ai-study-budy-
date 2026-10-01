""" Mini project => Ai Assistant"""
import pyttsx3
import datetime

def speak(audio):
    engine = pyttsx3.init("sapi5")
    engine.say(audio)
    engine.runAndWait()
    

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
        speak("Good morning ")

elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

elif hour >= 18 and hour < 20:
        speak("Good Evening")
else:
        speak("Good night")

    
speak("Welcome to our ai chatbot ")
print("Welcome to our ai chatbot ".center(50,"*"))
print("(Ask our question to get answer otherwise write bood bye to end communication)")

question_response = {
     "hello" : "Hey how can I help you",
    
     "how are you" : "I am good how about you",
     
     "what is your name" : "my name is AI Assistant",
     
     "who are you" : "I am AI Assistant What can you do I can answer question and help you with different task",
    
     "what is Python" : "Python is popular programming language",
    
     "what is AI" : "AI stands for Artificial Intelligence",
    
     "can you help me" : "of course tell me what you need help with",
    
     "thank you " : "you're welcome!",
    
     "bye" : "goodbye have a great day"}

def getreply(x):
    if x in question_response:
        return(question_response[question])
    else:
        return("Out of my mind ")

while True:
    question = input("User: ")
    reply = getreply(question.lower())
    speak(reply)
    print("chatbot:",reply)
    
    if question.lower() == "bye":
        break
     