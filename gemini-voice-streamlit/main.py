import io
import wave
import base64
import json
import streamlit as st
import speech_recognition as sr
import pyttsx3
import requests

# ------------------------------
# Gemini API Key
# ------------------------------
GEMINI_API_KEY = "AIzaSyC0rtvAp_P5iZwIE3_nzqrtn1VnpiT_HT8"

if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY is missing!")
    st.stop()

# ------------------------------
# Streamlit Page Setup
# ------------------------------
st.set_page_config(page_title="Gemini Voice Assistant", page_icon="🎙", layout="centered")
st.title("🎙 Gemini Voice Assistant")

# ------------------------------
# Record Audio
# ------------------------------
audio_file = st.audio_input("Press to record (hold to speak)")

if audio_file is not None:
    st.success("Captured audio!")

    # Save audio to temporary WAV file
    audio_bytes = audio_file.read()
    wav_path = "temp_audio.wav"
    with open(wav_path, "wb") as f:
        f.write(audio_bytes)

    # ------------------------------
    # Step 1: Transcribe audio to text
    # ------------------------------
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            transcribed_text = recognizer.recognize_google(audio_data)
            st.subheader("📝 You said:")
            st.write(transcribed_text)
        except sr.UnknownValueError:
            st.error("Could not understand audio")
            st.stop()
        except sr.RequestError as e:
            st.error(f"Speech Recognition error: {e}")
            st.stop()

    # ------------------------------
    # Step 2: Send text to Gemini
    # ------------------------------
    st.info("Generating response from Gemini...")

    payload = {
        "contents": [
            {"parts":[{"text": f"You are a helpful voice assistant. Respond concisely to: {transcribed_text}"}]}
        ]
    }

    response = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
        headers={
            "Content-Type": "application/json",
            "X-goog-api-key": GEMINI_API_KEY
        },
        data=json.dumps(payload)
    )

    if response.status_code != 200:
        st.error(f"Error from Gemini API: {response.text}")
        st.stop()

    resp_json = response.json()

    # Extract reply text
    reply_text = ""
    if resp_json.get("candidates"):
        parts = resp_json["candidates"][0]["content"]["parts"]
        reply_text = " ".join([p.get("text", "") for p in parts if p.get("text")])

    st.subheader("💬 Gemini says:")
    st.write(reply_text)

    # ------------------------------
    # Step 3: Convert reply to speech (local fallback using pyttsx3)
    # ------------------------------
    if reply_text:
        st.info("Generating speech locally...")

        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # speech rate
        engine.save_to_file(reply_text, "tts_output.wav")
        engine.runAndWait()

        # Play the generated WAV
        with open("tts_output.wav", "rb") as f:
            st.audio(f.read(), format="audio/wav")
