# ChatBot       :AAG
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
training_files = os.path.join(os.getcwd(),'english') #Path where training files are

for file in os.listdir(training_files):
    data = open(os.path.join(training_files,file)).readlines()
    bot.train(data)
    print('Talk to ChatBot')
    try:
        while True:
            text = input('You: ')
            reply = bot.get_response(text)
            print('Bot:',reply)
    except:
        print('GoodBye, Take Care')
