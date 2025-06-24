import pyttsx3
import streamlit as st
from readpdf import my_pdf


word = my_pdf()

engine = pyttsx3.init()
# # engine.say('Sally sells seashells by the seashore.')
engine.save_to_file(word, 'output_audio.wav')

engine.runAndWait()
st.audio("output_audio.wav")
st.audio("python_example_test.wav")



