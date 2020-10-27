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
print('\n this is a primitive Chatbot\nYou can ask your question right away!\n To stop send "quit')
chat = Chat(pairs)




# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak

while (True):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print('I am listening..')

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print('You: '+MyText)
            if(MyText=='quit' or MyText=='close'):
                print('SBC: Pleasure to meet you')
                SpeakText('pleasure to meet you')
                break

            print('SBC: '+chat.respond(MyText+'?'))
            SpeakText(chat.respond(MyText))

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Couldn't hear you")