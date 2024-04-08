import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pyttsx3
from utils.dicts import *
from utils.AutomateFuctions import DesktopAssistant
import questionary
from models.locals.Luna import luna
from rich.console import Console
from dotenv import load_dotenv, dotenv_values
import sys

sys.path.append('C:/Users/Hamdan/PycharmProjects/Luna')

console = Console()
AF = DesktopAssistant()
stop_commands = stop_commands
sites = sites
apps = apps
songs = songs
load_dotenv()

engine = pyttsx3.init()

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

content_generated = False

console.print("WARNING: Luna is currently under development,"
              "may be she can give error or some "
              "stupid behaviour while performing some tasks and she can make mistakes. Consider checking important "
              "information.\n", style="bold red")

method = questionary.select(
    message="Please select your interaction method with Luna from below:",
    choices=[
        "Cloud",
        "Local"
    ]
).ask()

if method == "Cloud":
    luna(None)