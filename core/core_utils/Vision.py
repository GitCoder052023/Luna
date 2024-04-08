import cv2
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import Markdown
import PIL.Image
from core.core_utils.audio_processing import recognize_audio
import pyttsx3
import os
from dotenv import load_dotenv, dotenv_values

engine = pyttsx3.init()
load_dotenv()


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key=os.getenv("Gemini_API_key"))
model = genai.GenerativeModel('gemini-pro-vision')


def Vision():
    url = 'http://192.168.1.2:4747/video'  # REPLACE WITH YOUR OWN DROID CAM IP ADDRESS
    cap = cv2.VideoCapture(url)
    frame_path = 'C:/Users/Hamdan/PycharmProjects/Gemini/Frames'  # Ensure this directory exists

    while True:
        engine.say("Started capturing, say capture to capture frame")
        engine.runAndWait()

        ret, frame = cap.read()

        if not ret:
            break  # End of video

        Input = recognize_audio(10, 20)

        if "capture" in Input.lower():
            engine.say("Ok sir")
            engine.runAndWait()

            frame_name = f"frame_{cap.get(cv2.CAP_PROP_POS_FRAMES)}.jpg"
            frame_path_full = pathlib.Path(frame_path) / frame_name
            cv2.imwrite(str(frame_path_full), frame)
            img = PIL.Image.open(frame_path_full)

            engine.say("frame captured!")
            engine.runAndWait()

            engine.say("Please ask questions")
            engine.runAndWait()

            Input = recognize_audio(10, 20)

        if Input.lower() == 'stop':
            break

        # Generate response from Gemini Pro Vision
        response = model.generate_content([Input, img], stream=True)
        response.resolve()
        print(response.text)
        engine.say(response.text)
        engine.runAndWait()

        if Input.lower() is None:
            print("")

    cap.release()
    cv2.destroyAllWindows()
