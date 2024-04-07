import pywhatkit
from utils.process_query import query_processer
from utils.audio_processing import recognize_audio
import pyttsx3
import webbrowser
import datetime
from utils.Weather import get_weather
from utils.news import get_news
from utils.dicts import *
from utils.os_functions import *
from utils.AutomateFuctions import DesktopAssistant

AF = DesktopAssistant()
stop_commands = stop_commands
sites = sites
apps = apps
songs = songs

engine = pyttsx3.init()

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')


def luna(e):
    content_generated = False

    while True:
        try:
            query = recognize_audio(10, 100)

            if query is not None:

                for site in sites:
                    if f"Open {site[0]}".lower() in query.lower():
                        engine.say(f"Opening {site[0]} sir...")
                        engine.runAndWait()
                        webbrowser.open(site[1])
                        content_generated = True

                for song in songs:
                    if f"play {song[0]}".lower() in query.lower():
                        engine.say(f"playing {song[0]} sir...")
                        engine.runAndWait()
                        webbrowser.open(song[1])
                        pywhatkit.playonyt(songs[1])
                        content_generated = True

                for app in apps:
                    if f"Open {app[0]}".lower() in query.lower():
                        engine.say(f"Opening {app[0]} sir")
                        engine.runAndWait()
                        if "Edge" in app[0]:
                            os.system(app[1])
                            content_generated = True
                        else:
                            os.startfile(app[1])
                            content_generated = True

                if any(command in query.lower() for command in stop_commands):
                    engine.say("Shutting down luna")
                    engine.runAndWait()

                    exit()

                elif "the time" in query.lower():
                    hour = datetime.datetime.now().strftime("%H")
                    minute = datetime.datetime.now().strftime("%M")
                    seconds = datetime.datetime.now().strftime("%S")
                    engine.say(f"Sir the time is {hour} hour, {minute} minutes, {seconds} seconds")
                    engine.runAndWait()

                elif "weather" in query.lower():
                    engine.say("sir, this is the report of today's weather")
                    get_weather("Lucknow")

                elif "search on youtube" in query.lower():
                    engine.say("sir, this is the result for your search")
                    # Remove text before and including "search on YouTube"
                    query = query.split("search on youtube", 1)[-1].strip()

                    # Create YouTube search URL
                    web = "https://www.youtube.com/results?search_query=" + query

                    # Open the YouTube search results in the default web browser
                    webbrowser.open(web)

                    # Play the first YouTube video based on the search query
                    pywhatkit.playonyt(query)
                    content_generated = True

                elif "today's news" in query.lower():
                    engine.say("sir, these are some top headlines of today")
                    engine.runAndWait()
                    get_news(api_key='REPLACE WITH YOUR OWN API KEY', category='general', country='in')

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

                elif "write this text" in query.lower():
                    engine.say("sure sir")
                    engine.runAndWait()

                    text_to_write = query.lower().split("write this text", 1)[-1].strip()
                    AF.type_text(text_to_write)

                elif "list my directory" in query.lower():
                    ld = list_directory_contents()

                    engine.say("sir, this is the list of your directory contents")
                    engine.runAndWait()

                    engine.say(ld)
                    engine.runAndWait()

                elif "create a new file" in query.lower():
                    engine.say("sir, please tell me the name for your file")
                    engine.runAndWait()

                    NFN = recognize_audio(5, 50)

                    create_file(NFN)

                    engine.say(f"sir, I created {NFN}")
                    engine.runAndWait()

                elif "Shutdown my" in query.lower():
                    engine.say("Are you sure sir?")
                    engine.runAndWait()

                    response = recognize_audio(5, 50)

                    if "yes" in response.lower():
                        engine.say("Shutting down system sir")
                        engine.runAndWait()

                        AF.ShutDown()

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


                elif "close this window" in query.lower():
                    engine.say("sure sir")
                    engine.runAndWait()

                    AF.close_current_window()

                elif "minimize this window" in query.lower():
                    engine.say("sure sir")
                    engine.runAndWait()

                    AF.minimize_current_window()

                elif "maximize this window" in query.lower():
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
            engine.runAndWait()  # code ends
