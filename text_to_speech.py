import pyttsx3
import streamlit as st
from readpdf import my_pdf

word = my_pdf()

engine = pyttsx3.init()

# save the audio as a wav file
engine.save_to_file(word, 'static/output_audio.wav')
engine.runAndWait()


