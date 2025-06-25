import streamlit as st
import fitz  # PyMuPDF
import pyttsx3
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Make sure 'static' directory exists
os.makedirs("static", exist_ok=True)

st.title("📄 PDF to Audio Converter")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    try:
        pdf_bytes = uploaded_file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        # Extract text from all pages
        text = ""
        for page in doc:
            text += page.get_text()

        st.subheader("📜 Extracted Text")
        st.text_area("PDF Text", text, height=400)

        if st.button("🔊 Convert to Audio and Play"):
            audio_file_path = "static/output_audio.wav"
            engine.save_to_file(text, audio_file_path)
            engine.runAndWait()

            st.success("✅ Audio file generated successfully!")
            st.audio(audio_file_path)

    except Exception as e:
        st.error(f"❌ Failed to process PDF: {e}")
        
else:
    st.info("Please upload a PDF file to get started.")
