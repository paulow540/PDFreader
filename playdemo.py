import streamlit as st
import fitz  # PyMuPDF
import pyttsx3
import os
import tempfile
import pandas as pd
from transformers import pipeline

# Initialize TTS engine
engine = pyttsx3.init()
os.makedirs("static", exist_ok=True)

# Optional NLP tools
summarizer = pipeline("summarization")

st.set_page_config(page_title="PDF Reader + TTS App", layout="wide")
st.title("📄 PDF Reader with Text-to-Speech and Summarization")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_bytes = uploaded_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    # Page selector
    page_numbers = list(range(1,len(doc)))
    selected_page = st.selectbox("Select Page to Read", page_numbers)
    page_text = doc[selected_page].get_text()

    st.subheader(f"📄 Extracted Text from Page {selected_page}")
    st.text_area("PDF Text", page_text, height=300)

    # Text summarization
    if st.button("🔍 Summarize Text"):
        with st.spinner("Summarizing..."):
            summary = summarizer(page_text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
            st.success("✅ Summary:")
            st.write(summary)

    # Text-to-speech
    if st.button("🔊 Convert to Audio"):
        audio_path = f"static/output_audio.wav"
        engine.save_to_file(page_text, audio_path)
        engine.runAndWait()
        st.success("Audio generated!")
        st.audio(audio_path)

    # Download audio
    with open("static/output_audio.wav", "rb") as file:
        st.download_button("⬇️ Download Audio", file, file_name="page_audio.wav")

    # Keyword frequency
    words = pd.Series(page_text.lower().split())
    common_words = words.value_counts().head(10)
    st.subheader("📊 Top 10 Keywords")
    st.bar_chart(common_words)

else:
    st.info("Please upload a PDF file to get started.")
