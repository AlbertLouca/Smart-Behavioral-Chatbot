import pandas as pd
import speech_recognition as sr
import pyttsx3
from nltk.chat.util import Chat, reflections

data = pd.read_csv('WikiQA.tsv', sep='\t')
questions_Answers = data[['QuestionID', 'Question', 'Sentence']]
pairs = []  # the big list of pairs(question/answers
i = 0  # number of loop
question_no = 0
answer_concatenated = 'Hello'
previous_question = 'Hi'
for x, y, z in zip(questions_Answers['QuestionID'].values, questions_Answers['Question'].values,
                   questions_Answers['Sentence'].values):
    # x = the question id
    # y = the question
    # z = the answer
    i = i + 1
    if i == 900000:
        break
    if x == question_no:
        answer_concatenated = answer_concatenated + '\n' + z
        previous_question = y
    else:
        answers_list = [answer_concatenated]
        question_list = [previous_question, answers_list]

        pairs.append(question_list)
        question_no = x
        answer_concatenated = z
print('\n this is a primitive Chatbot\nYou can ask your question right away!\n To stop Say "Quit or Stop"')
chat = Chat(pairs)





r = sr.Recognizer()

def SpeakText(command):# Function to convert text to speech
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
while (True):
    try:
        # use the microphone as source for input.
        with sr.Microphone() as user_voice:
            r.adjust_for_ambient_noise(user_voice, duration=0.2)
            print('SBC: I am listening..')
            audio2 = r.listen(user_voice)
            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print('You: '+MyText)
            if(MyText=='quit' or MyText=='stop'):
                print('SBC: Pleasure to meet you')
                SpeakText('pleasure to meet you')
                break
                if(chat.respond(MyText+'?')==None):
                    print('SBC: Sorry i don"t know the answer')
                    continue
            print(chat.respond(MyText+'?'))
            SpeakText(chat.respond(MyText))
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Couldn't Hear you")