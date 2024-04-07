from core_utils.process_query import query_processer
from core_utils.audio_processing import recognize_audio
import pyttsx3
import webbrowser
import datetime
from core_utils.Weather import get_weather
from core_utils.news import get_news
from core_utils.process_query import write_mail
import smtplib
from core_utils.dicts import *
from core_utils.os_functions import *
from core_utils.AutomateFuctions import DesktopAssistant
from core_utils.SendWhatMessage import *
from core_utils.scheduler import task_scheduler
from core_utils.TextBasedLuna import Activate_LunaTXT
from core_utils.Vision import Vision

AF = DesktopAssistant()
stop_commands = stop_commands
sender_email = sender_email
sender_password = sender_password
sites = sites
songs = songs

engine = pyttsx3.init()

content_generated = False

print("Luna is currently under development,"
      "So, may be you got an error or some "
      "stupid behaviour while performing some tasks and you got some changes, improvements, and"
      " additional"
      "features in Luna!")

print("Dear user, \nPlease select the model to chat from below: \nText based Luna: LunaTXT \nVoice Based Luna: LunaVOC")
print("")

model = input("Please choose the model to chat from above: ")

if model == "LunaTXT":
    print("Welcome to LunaTXT!")

    Activate_LunaTXT()

if model == "LunaVOC":
    print("Welcome to LunaVOC")

    while True:
        try:
            query = recognize_audio(10, 100)

            if query is not None:

                if "hello luna" in query.lower():
                    engine.say("Hello sir, I am Luna, Your personal AI assistant. How can I help you today?")
                    engine.runAndWait()

                elif "How are you luna" in query.lower():
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

                elif "about your updates" in query.lower():
                    engine.say("Sir, currently I am updated with these 2 new features which, 1st is Text based version"
                               "of me, and 2nd is vision feature of me. Sir the 1st feature of me allows you to chat"
                               "with me on text, this feature is added in me to maintain your privacy, but sir in text "
                               "model you can only ask questions, You don't have a access of my other capabilities. And"
                               "sir the second feature of me is vision capability is added in me, this capability "
                               "allows"
                               "me to see the things and then answer the questions related to the things.")

                elif "start your vision" in query.lower():
                    Vision()

                for site in sites:
                    if f"Open {site[0]}".lower() in query.lower():
                        engine.say(f"Opening {site[0]} sir...")
                        engine.runAndWait()
                        webbrowser.open(site[1])
                        exit()

                for song in songs:
                    if f"play {song[0]}".lower() in query.lower():
                        engine.say(f"playing {song[0]} sir...")
                        engine.runAndWait()
                        webbrowser.open(song[1])
                        pywhatkit.playonyt(songs[1])
                        exit()

                if any(command in query.lower() for command in stop_commands):
                    print("Shutting down luna")
                    exit()

                elif "the time" in query.lower():
                    hour = datetime.datetime.now().strftime("%H")
                    minute = datetime.datetime.now().strftime("%M")
                    seconds = datetime.datetime.now().strftime("%S")
                    engine.say(f"Sir the time is {hour} hour, {minute} minutes, {seconds} seconds")
                    engine.runAndWait()

                elif "weather" in query.lower():
                    engine.say("sir, this is the report of today's weather")
                    get_weather()

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
                    break

                elif "today news" in query.lower():
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

                elif "list my directory" in query.lower():
                    ld = list_directory_contents()

                    engine.say("sir, this is the list of your directory contents")
                    engine.runAndWait()

                    print(ld)

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

                    print("listening...")
                    file = recognize_audio(5, 50)

                    engine.say("sir, what is the new name for your file?")
                    engine.runAndWait()

                    print("listening...")
                    RFN = recognize_audio(5, 50)

                    rename_file_or_folder(file, RFN)

                    engine.say(f"sir, I renamed {file} to {RFN}")
                    engine.runAndWait()

                elif "check file exists or not" in query.lower():
                    engine.say("sure sir, what is the name of your file?")
                    engine.runAndWait()

                    print("Listening...")
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

                    print("Listening...")
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

                elif "send whatsapp message" in query.lower():
                    engine.say("sure sir, please enter the name of person")
                    engine.runAndWait()

                    name = input("Please Enter name: ")

                    engine.say("sure sir, now please speak the message you want to send")
                    engine.runAndWait()

                    WM = recognize_audio(20, 50)

                    engine.say("sure sir, now I am sending whatsapp message")
                    engine.runAndWait()

                    send_whatsapp_message(name, WM)

                elif "schedule" in query.lower():
                    engine.say("sure sir, please speak your task to schedule")
                    engine.runAndWait()

                    sch = recognize_audio(10, 50)

                    engine.say("ok sir, now please enter the date and time in this format")
                    engine.runAndWait()

                    print("%Y-%m-%d %H:%M")
                    print("")

                    tm = input("Enter time: ")

                    engine.say(f"sure sir, I scheduled your task I will inform you on time")
                    engine.runAndWait()

                    tsk = task_scheduler(sch, tm)

                    engine.say(tsk)
                    engine.runAndWait()

                elif "send mail" in query.lower():
                    engine.say("Sir, do you want to write gmail using artificial intelligence?")
                    engine.runAndWait()
                    print("Listening...")

                    wish = recognize_audio(3, 100)
                    print("Processing...")

                    if "yes" in wish.lower():
                        engine.say("Sir, please give me the topic of gmail")
                        engine.runAndWait()

                        topic = recognize_audio(10, 100)

                        engine.say("Writing email sir...")
                        engine.runAndWait()

                        mail = write_mail(topic)
                        print("Mail: " + mail)

                        sendMail = input("Sir, do you want to send this email [Y/n]: ")

                        if sendMail == "Y":
                            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
                            smtp_server.starttls()
                            smtp_server.login(sender_email, sender_password)

                            # Compose the email
                            from_address = sender_email
                            to_address = input("Sir, please enter recipient email: ")
                            subject = input("Sir, please enter the subject of your email: ")
                            body = mail

                            email_message = f'Subject: {subject}\n\n{body}'

                            engine.say("sending email sir to", to_address)
                            engine.runAndWait()
                            # Send the email
                            smtp_server.sendmail(from_address, to_address, email_message)

                            # Close the SMTP server connection
                            smtp_server.quit()

                            engine.say("Sir Email sent successfully!")
                            engine.runAndWait()

                        if sendMail == "n":
                            engine.say("Sorry sir, you can write your mail yourself")
                            engine.runAndWait()

                            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
                            smtp_server.starttls()
                            smtp_server.login(sender_email, sender_password)

                            # Compose the email
                            from_address = sender_email
                            to_address = input("Sir, please enter recipient email: ")
                            subject = input("Sir, please enter the subject of your email: ")
                            body = input("Write your email: ")

                            email_message = f'Subject: {subject}\n\n{body}'

                            engine.say("sending email sir to", to_address)
                            engine.runAndWait()
                            # Send the email
                            smtp_server.sendmail(from_address, to_address, email_message)

                            # Close the SMTP server connection
                            smtp_server.quit()

                            engine.say("Sir Email sent successfully!")
                            engine.runAndWait()

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
