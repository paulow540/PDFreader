# 📄🔊 Streamlit PDF-to-Audio App

This is a simple and powerful web app built with **Python** and **Streamlit** that lets users:

✅ Upload a PDF  
✅ Extract all text from the PDF  
✅ Convert the extracted text into speech  
✅ Save it as a `.wav` audio file  
✅ Play the audio file directly in the app

---

## 🚀 Demo

![PDF to Audio Demo](demo.gif)  
> 🎧 [Click to listen to sample audio]([https://github.com/paulow540/PDFreader/blob/main/output_audio.wav](https://github.com/paulow540/PDFreader/blob/main/python_example_test.wav))


---

## 🛠️ Features

- Upload PDF files
- Extract and preview PDF text
- Convert text to speech using `pyttsx3`
- Save speech as `.wav` file
- Audio playback in Streamlit

---

## 📦 Tech Stack

- **Streamlit** – Web app interface  
- **PyMuPDF / fitz** – PDF text extraction  
- **pyttsx3** – Text-to-speech engine  
- **Python Standard Libraries**

---

## 🖥️ Installation

```bash
git clone https://github.com/yourusername/pdf-to-audio-app.git
cd pdf-to-audio-app
pip install -r requirements.txt
streamlit run app.py
