## Smart-Behavioral-Chatbot

![alt text](https://github.com/AlbertLouca/Smart-Behavioral-Chatbot/blob/main/Untitled.png)

Our system aims to better and feather enhance the chatbot technology through making it a smart behavioral one that can carry a conversation smoothly and efficiently with humans using Deep Reinforcement Learning, Image and video processing .Through conversing with said human it can not only process his/her words with remarkable accuracy but also their behavior during said words (ex. Angry ,sad , frustrated )through image and voice processing to reply accordingly in which our system will go through different sources and then compile together the most fitting reply/answer through the use of deep reinforcement learning giving the user the feeling that he/she is talking to a conscious human being.Input wise The user will use a video camera and a microphone to converse with our chatbot.After that the system will extract the frames and audio out of the video so that we can have our data.The processing of both the audio and the frames acquired from the live video will be simultaneous. Using speech recognition the system will turn the spoken words into text (string) form so that the system can understand what the user's inquiry is about. Analyze user speech to extract vocal sentimental features by analyzing multiple physical proprieties of the voice said famously the "Empath" AI uses such technique. Then on the other side the system will make use of face detection techniques / algorithms to locate the face making extracting information about his/her stat easier . Through the use of machine learning the system will be able to detect the user emotions using techniques such as recognize feature point acquired from the user's face in order to detect his/her emotional stat across the duration that he/she is conversing with the system bot and comparing them to our dataset.Finally through the use of the data we collected and deep reinforcement learning the user will be presented with the most fitting reply that will make the conversation between him/her and the system bot flow smoothly as if it was carried by a human.



## Our Model consist of two main phases:

### Text Classification using BERT:
Our augmented data-set consists of 4115  questions all of them are categorized into 14 categories which are ( 'Speculation','Transmission', 'Nomenclature', 'Reporting','Societal      Response', 'Societal Effects', 'Origin', 'Prevention',
    'Treatment', 'Testing', 'Comparison', 'Economic Effects',
    'Symptoms', 'Having COVID', 'Individual Response' ). 75% of them are used in training while 25\% are used in testing.  we start the pre-processing part where we collect all the questions associated with a specific category which corresponds to the column in the data-set and then we train our model on all the questions.
    The implementation of the BERT model here is after we train our model and start using it by giving it the questions as an input and the model will respond with the right category in which we take the context file associated with it and feed it to the next part.the objective from this step is to classify the type of inquiry the user want so it would be easier and faster for the QnA model to answer the question with good accuracy as well as allowing as to have more organized and suitable data set.While training we reached accuracy about 98\% and testing about 96% as shown in Fig.2.
    it's clear that our Bert classifier has a bit of over fitting.
    
###  Answering questions using BERT:


The second model(QnA with BERT) which is pre-trained toreceive 512 token in the form of text as the maximum number.BERT  is  developed  to  understand  the  context  of  a  paragraphand to take the question as the input and and get the answerfrom  the  provided  context.  The  model  predicts  the  start  andend tokens from the paragraph which is given to it in the formof the context that will most likely answer the given question



Bidirectional  Encoder  Representations  from  Transformers(BERT) is considered a Transformer based on machine learn-ing techniques for natural language processing purposes (NLP) already  pre-trained  and  developed  by  Google  researchers.BERT was developed to help with Q&A tasks using a questionand answer dataset like SQuAD v2.0. BERT is different thansomething like LSTM in some points where it takes the wholesentence as the input and not the words sequentially so it takesboth  of  the  question  and  the  context  in  a  specific  tasks  likequestion answering ones where it needs to be fine tuned afterbeing pre-trained by google.
