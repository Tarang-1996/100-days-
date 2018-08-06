from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from chatterbot.filters import RepetitiveResponseFilter

bot = ChatBot('Bot')

bot.set_trainer(ListTrainer)

for file in os.listdir('C:/Users/TARANG/Documents/GitHub/100-days-code-challenge/100-days-/education/'):
    data = open('C:/Users/TARANG/Documents/GitHub/100-days-code-challenge/100-days-/education/'+ file ,'r').readlines()
    bot.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot :',reply)
    if message.strip() == 'Bye':
        print('ChatBot : Bye')
        break



