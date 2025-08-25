# 🎙 Gemini Voice Assistant (Streamlit)

This is a **voice assistant** built with **Streamlit** that uses **Google Gemini API** for text generation. It allows you to:

1. Record your voice directly in the browser.
2. Convert your voice to text using **speech recognition**.
3. Send the text to **Gemini** for a concise response.
4. Play the response using **local TTS** (`pyttsx3`) to avoid API quota issues.

---

## 🔹 Features

- **Audio Recording:** Record your voice with Streamlit’s `audio_input`.
- **Speech-to-Text:** Transcribes audio using the `speech_recognition` library.
- **Text Generation:** Sends transcribed text to **Google Gemini** API for a response.
- **Text-to-Speech:** Converts Gemini’s reply to audio locally using `pyttsx3`.
- **Streamlit UI:** Clean interface for recording, displaying, and listening.

---

## 🛠 Prerequisites

- Python 3.9+
- Streamlit
- Requests
- SpeechRecognition
- PyAudio (for microphone support)
- pyttsx3
- (Optional) `pyaudio` installation may require additional OS dependencies.

---

## ⚡ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/devyaniraghatate/gemini-voice-assistant.git
cd gemini-voice-assistant
```
---

## Setup

Open the main Python file (app.py) and replace the placeholder with your Google Gemini API key:
```
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Ensure your microphone is working.

----

## Running the Application
```
streamlit run app.py
```

The app will open in your browser. Press and hold the record button to speak. The assistant will transcribe your speech, send it to Gemini, and play the response using local TTS.

## Notes

Gemini TTS free tier is limited. Local TTS (pyttsx3) is used to avoid hitting API limits.

Speech recognition requires a working microphone and internet access for high-quality transcription.
