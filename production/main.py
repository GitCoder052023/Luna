import flet as ft
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import warnings
import pywhatkit
from audio_processing import recognize_audio
import pyttsx3
import webbrowser
import datetime
from Weather import get_weather
from news import get_news
from dicts import *
from os_functions import *
from AutomateFuctions import DesktopAssistant
import google.generativeai as genai

key = "REPLACE WITH YOUR OWN GEMINI API KEY"
model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True,
                               google_api_key=key, temperature=1.0)


def query_processer(query_source):
    user_query = query_source
    response = model(
        [
            SystemMessage(
                content=f"""You are a virtual desktop assistant and your name is "Luna" and you are developed by "Hamdan", Now anser this quesion and if this question asks about you then introduce your self as "Luna": {user_query}"""
            ),
            HumanMessage(content=user_query),
        ]
    )

    return response.content


warnings.filterwarnings("ignore")
AF = DesktopAssistant()
stop_commands = stop_commands
sites = sites
songs = songs
engine = pyttsx3.init()

content_generated = False

try:
    class Message():
        def __init__(self, user_name: str, text: str, message_type: str):
            self.user_name = user_name
            self.text = text
            self.message_type = message_type


    class ChatMessage(ft.Row):
        def __init__(self, message: Message):
            super().__init__()
            self.vertical_alignment = "start"
            self.controls = [
                ft.CircleAvatar(
                    content=ft.Text(self.get_initials(message.user_name)),
                    color=ft.colors.WHITE,
                    bgcolor=self.get_avatar_color(message.user_name),
                ),
                ft.Column(
                    [
                        ft.Text(message.user_name, weight="bold"),
                        ft.Text(message.text, selectable=True),
                    ],
                    tight=True,
                    spacing=5,
                ),
            ]

        def get_initials(self, user_name: str):
            return user_name[:1].capitalize()

        def get_avatar_color(self, user_name: str):
            colors_lookup = [
                ft.colors.AMBER,
                ft.colors.BLUE,
                ft.colors.BROWN,
                ft.colors.CYAN,
                ft.colors.GREEN,
                ft.colors.INDIGO,
                ft.colors.LIME,
                ft.colors.ORANGE,
                ft.colors.PINK,
                ft.colors.PURPLE,
                ft.colors.RED,
                ft.colors.TEAL,
                ft.colors.YELLOW,
            ]
            return colors_lookup[hash(user_name) % len(colors_lookup)]


    def Text(page: ft.Page):
        page.horizontal_alignment = "stretch"
        page.title = "Luna - TextModel"

        def join_chat_click(e):
            if not join_user_name.value:
                join_user_name.error_text = "Name cannot be blank!"
                join_user_name.update()
            else:
                page.session.set("user_name", join_user_name.value)
                page.dialog.open = False
                new_message.prefix = ft.Text(f"{join_user_name.value}: ")
                page.pubsub.send_all(Message(user_name=join_user_name.value,
                                             text=
                                             f"{join_user_name.value}+has joined the chat.",
                                             message_type="login_message"))
                page.update()

        def send_message_click(e):
            if new_message.value != "":
                page.pubsub.send_all(Message(page.session.get(
                    "user_name"), new_message.value, message_type="chat_message"))
                temp = new_message.value
                new_message.value = ""
                new_message.focus()
                res = model(temp)
                if len(res) > 220:  # adjust the maximum length as needed
                    res = '\n'.join([res[i:i + 220]
                                     for i in range(0, len(res), 220)])
                page.pubsub.send_all(
                    Message("Luna", res, message_type="chat_message"))
                page.update()

        def model(query_source):
            messages = []

            while True:
                query = query_source

                genai.configure(api_key="AIzaSyBoxqElIKXzz7IxkiEllxyDQlYbasCkbTc")

                model = genai.GenerativeModel('gemini-pro')

                message = query
                messages.append({
                    "role": "user",
                    "parts": [message],
                })

                response = model.generate_content(messages)

                messages.append({
                    "role": "model",
                    "parts": [response.text],
                })

                return response.text

        def on_message(message: Message):
            if message.message_type == "chat_message":
                m = ChatMessage(message)
            elif message.message_type == "login_message":
                m = ft.Text(message.text, italic=True,
                            color=ft.colors.BLACK45, size=12)
            chat.controls.append(m)
            page.update()

        page.pubsub.subscribe(on_message)

        # A dialog asking for a user display name
        join_user_name = ft.TextField(
            label="Enter your name to join the chat",
            autofocus=True,
            on_submit=join_chat_click,
        )
        page.dialog = ft.AlertDialog(
            open=True,
            modal=True,
            title=ft.Text("Welcome!"),
            content=ft.Column([join_user_name], width=300, height=70, tight=True),
            actions=[ft.ElevatedButton(
                text="Join chat", on_click=join_chat_click)],
            actions_alignment="end",
        )

        # Chat messages
        chat = ft.ListView(
            expand=True,
            spacing=10,
            auto_scroll=True,
        )

        # A new message entry form
        new_message = ft.TextField(
            hint_text="Write a message...",
            autofocus=True,
            shift_enter=True,
            min_lines=1,
            max_lines=5,
            filled=True,
            expand=True,
            on_submit=send_message_click,
        )

        # Add everything to the page
        page.add(
            ft.Container(
                content=chat,
                border=ft.border.all(1, ft.colors.OUTLINE),
                border_radius=5,
                padding=10,
                expand=True,
            ),
            ft.Row(
                [
                    new_message,
                    ft.IconButton(
                        icon=ft.icons.SEND_ROUNDED,
                        tooltip="Send message",
                        on_click=send_message_click,
                    ),
                ]
            ),
        )


    async def main(page: ft.Page):
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.appbar = ft.AppBar(title=ft.Text("Hello sir, How can I help you today?"), center_title=True)

        async def handle_start_recording(e):
            global content_generated
            engine.say("Hello sir, I am Luna, Your personal AI assistant. How can I help you today?")
            engine.runAndWait()

            while True:
                try:
                    query = recognize_audio(10, 100)

                    if query is not None:

                        if "hello" in query.lower():
                            engine.say("Hello sir, I am Luna, Your personal AI assistant. How can I help you today?")
                            engine.runAndWait()

                        elif "How are you" in query.lower():
                            engine.say("Sorry sir, but I am machine and I don't have a feelings and emotions")
                            engine.runAndWait()

                        elif "yourself" in query.lower():
                            engine.say(
                                "Sir, I am able to do many tasks like Opening websites, playing song, sending gmail,"
                                "telling time, answering your questions, performing YouTube search, etc"
                                "But sir,"
                                "all these tasks are personal tasks. not only these tasks but I am able to do local things on "
                                "your"
                                "computer"
                                " which can "
                                "you think."
                                " But sir I am currently under development,"
                                "So, may be you got an error or some "
                                "stupid behaviour by me while performing some tasks and you got some changes, improvements, and"
                                " additional"
                                "features in me")
                            engine.runAndWait()

                        for site in sites:
                            if f"Open {site[0]}".lower() in query.lower():
                                engine.say(f"Opening {site[0]} sir...")
                                engine.runAndWait()
                                webbrowser.open(site[1])
                                os.remove("hello.mp3")
                                exit()

                        for song in songs:
                            if f"play {song[0]}".lower() in query.lower():
                                engine.say(f"playing {song[0]} sir...")
                                engine.runAndWait()
                                webbrowser.open(song[1])
                                pywhatkit.playonyt(songs[1])
                                os.remove("hello.mp3")
                                exit()

                        if any(command in query.lower() for command in stop_commands):
                            engine.say("Shutting down luna")
                            engine.runAndWait()
                            os.remove("hello.mp3")
                            exit()

                        elif "the time" in query.lower():
                            hour = datetime.datetime.now().strftime("%H")
                            minute = datetime.datetime.now().strftime("%M")
                            seconds = datetime.datetime.now().strftime("%S")
                            engine.say(f"Sir the time is {hour} hour, {minute} minutes, {seconds} seconds")
                            engine.runAndWait()

                        elif "weather" in query.lower():
                            engine.say("sir, this is the report of today's weather")
                            engine.runAndWait()
                            get_weather()

                        elif "search on youtube" in query.lower():
                            engine.say("sir, this is the result for your search")
                            engine.runAndWait()
                            # Remove text before and including "search on YouTube"
                            query = query.split("search on youtube", 1)[-1].strip()

                            # Create YouTube search URL
                            web = "https://www.youtube.com/results?search_query=" + query

                            # Open the YouTube search results in the default web browser
                            webbrowser.open(web)

                            # Play the first YouTube video based on the search query
                            pywhatkit.playonyt(query)
                            break

                        elif "today news" in query.lower():
                            engine.say("sir, these are some top headlines of today")
                            engine.runAndWait()
                            get_news(api_key="fba484ce7b034a7ba08cbe6e6f8a1b8f", category='general', country='in')

                        elif "what is my current working directory" in query.lower():
                            cwd = get_current_dir()

                            engine.say(f"sir, your current working directory is, {cwd}")
                            engine.runAndWait()

                        elif "create a new directory" in query.lower():
                            engine.say("sir please give the name to your directory")
                            engine.runAndWait()

                            nd = recognize_audio(5, 50)
                            cd = create_directory(nd)

                            engine.say(f"sir, I created {nd}")
                            engine.runAndWait()

                        elif "list my directory" in query.lower():
                            ld = list_directory_contents()

                            engine.say("sir, this is the list of your directory contents")
                            engine.runAndWait()

                            ft.Text(value=ld)

                        elif "create a new file" in query.lower():
                            engine.say("sir, please tell me the name for your file")
                            engine.runAndWait()

                            NFN = recognize_audio(5, 50)

                            create_file(NFN)

                            engine.say(f"sir, I created {NFN}")
                            engine.runAndWait()

                        elif "rename my file" in query.lower():
                            engine.say("sir, what is the name of your file?")
                            engine.runAndWait()

                            file = recognize_audio(5, 50)

                            engine.say("sir, what is the new name for your file?")
                            engine.runAndWait()

                            RFN = recognize_audio(5, 50)

                            rename_file_or_folder(file, RFN)

                            engine.say(f"sir, I renamed {file} to {RFN}")
                            engine.runAndWait()

                        elif "check file exists or not" in query.lower():
                            engine.say("sure sir, what is the name of your file?")
                            engine.runAndWait()

                            CFN = recognize_audio(5, 50)

                            results = check_file_existence(CFN)

                            if results == "True":
                                engine.say(f"Yes sir, {CFN} is exists in your device")
                                engine.runAndWait()

                            if results != "True":
                                engine.say(f"No sir, {CFN} does not exist on your device.")
                                engine.runAndWait()

                        elif "check file size" in query.lower():
                            engine.say("sure sir, what is the name of your file?")
                            engine.runAndWait()

                            CFS = recognize_audio(5, 50)

                            resl = get_file_size(CFS)

                            engine.say(f"sir your file size is {resl}")
                            engine.runAndWait()

                        elif "take screenshot" in query.lower():
                            engine.say("sure sir, but please give the name to your screenshot")
                            engine.runAndWait()

                            SN = recognize_audio(5, 50)

                            AF.screenshot(f"{SN}.png")

                            engine.say(f"sir I saved {SN}.png")
                            engine.runAndWait()

                        elif "search on google" in query.lower():
                            engine.say("sure sir, please tell me the topic to search on google")
                            engine.runAndWait()

                            GT = recognize_audio(10, 50)

                            AF.search_on_google(GT)

                            engine.say("sir, this is the result from google")
                            engine.runAndWait()

                        elif "close current window" in query.lower():
                            engine.say("sure sir")
                            engine.runAndWait()

                            AF.close_current_window()

                        elif "minimize current window" in query.lower():
                            engine.say("sure sir")
                            engine.runAndWait()

                            AF.minimize_current_window()

                        elif "maximize current window" in query.lower():
                            engine.say("sure sir")
                            engine.runAndWait()

                            AF.maximize_current_window()


                        else:
                            if not content_generated:
                                # Set the flag to True

                                content_generated = True

                                # Generate content

                                content = query_processer(query)

                                # Speak the content

                                engine.say("sir," + content)

                                engine.runAndWait()

                                # If content has already been generated, skip this condition
                            else:
                                print("")
                                pass
                                content_generated = False

                except:
                    engine.say("")
                    engine.runAndWait()

        # **Modified section for larger icon button**
        large_icon_button = ft.IconButton(
            icon=ft.icons.MIC,
            on_click=handle_start_recording,
            icon_size=100
            # Adjust this value to set desired size
        )

        current_content = None

        async def change_content(e):
            global current_content

            page.controls.clear()
            nav_dest = e.control.selected_index

            if nav_dest == 0:
                nav_content = ft.Container(
                    content=ft.app(target=main)
                )
                if current_content:
                    page.controls.remove(current_content)
                await page.add_async(nav_content)
                current_content = nav_content
            elif nav_dest == 1:
                nav_content = ft.Container(
                    content=ft.app(target=Text)
                )
                if current_content:
                    page.controls.remove(current_content)
                await page.add_async(nav_content)
                current_content = nav_content

        nav = page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.MIC, label="Luna-V0C"),
                ft.NavigationDestination(icon=ft.icons.TEXTSMS, label="Luna-TeXT")
            ],
            on_change=change_content
        )

        await page.add_async(large_icon_button)
        await page.add_async(nav)


    ft.app(target=main)


except:
    print("")

# pyinstaller --name Luna --onefile --windowed --icon=logo.ico main.py
