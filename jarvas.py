from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib


def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')
#listen for commands

def myCommand():
     r = sr.Recognizer()

     with sr.Microphone() as source:
         print('I am ready for your next command')
         r.pause_threeshold = 1
         r.adjust_for_ambient_noise(source,duration = 1)

     try:
         command = r.recognize_google(audio)
         print('You said:' + command + '/n')
# loop back to con to listen command
     except sr.UnknownValueError:
         assistant(myCommand())

     return command
#if statement for executing commands
def assistant(command):

    if 'open Reddit python' in command:
        chrome_path = ''
        url = 'https://www.reddit.com'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('who is the recipient')

    if 'email' in  command:
         talkToMe('what should I say')
         content = myCommand()

         #init gmail
         mail = smtplib.SMTP('smtp.gmail.com',587)

         #identify to server
         mail.ehlo()

         #encrpt session
         mail.starttls()

         #login
         mail.login('username','password')

         #send message
         mail.sendmail('Gaurav','gauravpal7710@gmail.com','hello')

         #mail.close
         mail.close()

         talkToMe('Email sent')
talkToMe('I am ready')

while True:
    assistant(myCommand())
         
