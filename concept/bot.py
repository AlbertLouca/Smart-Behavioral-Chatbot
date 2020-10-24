import pandas as pd

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

print('\nthis is a primitive Chatbot\nYou can ask your question right away!\n To stop send "quit')
chat = Chat(pairs)
#print(chat.respond('hi  '))


chat.converse()

