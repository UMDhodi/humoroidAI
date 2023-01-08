import random

command_1 = ['hello',
'wake up',
'hey',
'hey there',
'humoroid',
'hi']

reply_1 = ['Hello sir, Welcome back mayank sir !',
'Always for you sir',
'Oh ! hi sir,'
'Hey, how are you',
'Whats up ! sir',
'Hello sir, today weather nice']

command_2 = ['ok you can sleep',
'thank you',
'ok thanks',
'okay',
'ok',
'okay bye',
'bye',
'shutdown yourself',
'i will see you later',
'catch you later']

reply_2 = ['Okay ! sir',
'Okay sir i will see you later !',
'Okay !',
'Bye sir !',
'As your wish sir !',
'Have a good day sir...',
'It would be great meeting you again sir, bye',
'Okay sir ! If you have any work for me i am ready any time every minute',]


def Chatterbot(text):
    for word in text.split():

        if word in command_1:
            return random.choice(reply_1) + "."

        elif word in command_2:
            return random.choice(reply_2) 