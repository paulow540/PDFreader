import pyttsx3
from ppdf import my_pdf

word = my_pdf()

engine = pyttsx3.init()
# # engine.say('Sally sells seashells by the seashore.')
engine.say(word)
engine.runAndWait()