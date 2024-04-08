import speech_recognition as sr
import os
from dotenv import load_dotenv, dotenv_values
import assemblyai as aai

load_dotenv()
aai.settings.api_key = os.getenv("Assembly_API_key")
transcriber = aai.Transcriber()


def recognize_audio(duration, threshhold=250):
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        r.energy_threshold = threshhold
        with sr.Microphone() as source:
            audio = r.record(source, duration=duration)

        # write audio to a mp3 file
        with open("hello.mp3", "wb") as f:
            f.write(audio.get_wav_data())

        # recognize audio using AssemblyAI
        transcript = transcriber.transcribe("hello.mp3")

        # delete the previous mp3 file
        os.remove("hello.mp3")
        return transcript.text
