# Luna: Your Personal AI Assistant

## Description
Luna is a versatile AI assistant designed to make your life easier by automating tasks, providing information, and managing your digital life. She can respond to your voice commands to perform a wide range of actions, including:

- Opening websites and applications
- Playing music
- Sending emails
- Telling the time
- Providing weather updates
- Searching the web
- Getting news headlines
- Managing files and folders
- Taking screenshots
- Automating desktop tasks
- Sending WhatsApp messages
- Scheduling tasks
- Computer Vision

 ## Basic Structure

 The code is organized into several modules:

- main.py: The main program file that handles the core functionality and user interaction.
- process_query.py: Contains functions for processing user queries and generating responses.
- audio_processing.py: Handles audio input and speech recognition.
- Weather.py: Retrieves weather information.
- news.py: Fetches news headlines.
- os_functions.py: Contains functions for interacting with the operating system (e.g., managing files and folders).
- AutomateFuctions.py: Provides functions for automating desktop tasks.
- SendWhatMessage.py: Enables sending WhatsApp messages.
- scheduler.py: Handles task scheduling.

 ## Key Features

- Voice-controlled interface: Interact with Luna using natural language commands.
- Wide range of functionalities: Perform various tasks, from basic information retrieval to managing your computer.
- Email capabilities: Compose and send emails, including the option to use AI-generated content.
- File management: Create, rename, delete, and check files and folders.
- Desktop automation: Control windows and applications, take screenshots, and more.
- WhatsApp integration: Send WhatsApp messages directly from Luna.
- Task scheduling: Set reminders and schedule tasks for Luna to execute at specific times.

# Setup

## Setup API keys And Passwords


Here are the instructions for setting up the API keys required for Luna:

1. **Google Gemini API:**

- Visit the Google AI Studio: https://makersuite.google.com/app/apikey
- Click on Create new API Key.
- Save your API key securly 

2. **News API:**

- Create a free account at https://newsapi.org/.
- Obtain your API key from your account dashboard.
- Paste your API key in the main.py today news function

3. **Weather API:**

Obtain a Free API Key:

- Visit the OpenWeatherMap website: https://openweathermap.org/api
- Create a free account or log in if you already have one.
- Go to the "API Keys" section in your account settings.
- Copy your API key.

Add Your API Key to the Code:

- Open the Python code file (Weather.py).
- Locate the line api_key = "REPLACE WITH YOUR OWN API KEY".
- Replace the placeholder text with your actual API key.

**Assembly AI API:**

- Visit the AssemblyAI website at https://www.assemblyai.com/
- Click on the "Sign Up" button in the top right corner.
- Enter your email address, password, and other required information.
- Click on the "Create Account" button.

2. Obtain Your API Key:

- Once you've logged in, you'll be taken to your dashboard.
- Your API key will be displayed prominently under the "Your API key" section.
- Click the "copy" icon to copy the key to your clipboard.

3. Add the API Key to Your audio processing.py File:

- Open audio processing.py file.
- Paste the copied API key into the **REPLACE WITH YOUR OWN ASSEMBLY AI API KEY**.

**Create App password for gmail**

- To generate app password you need to open your gmail and click on your "profile button"
- And then click on "manage your google account" button and make sure that you have already doned "2 step varification"
- And then search for "app password" in search box.
- And then create a random name for your app passwored for example "Python", and then copy the app passwored provided by google and paste it in dicts.py

## Setting up required libraries

1. Install the required libraries:
   ```bash
   pip install pyttsx3==2.71 webbrowser datetime pywhatkit smtplib newsapi-python requests google-generativeai pyaudio PyAutoGUI
   ```
 
2. Make changes file named dicts.py and define the following variables
   ```Python
   sender_email = "your_email@gmail.com"
   sender_password = "your_email_password"
   ```

3. Run the main program:
   ```bash
   python main.py
   ```

# Usage
Speak a command to Luna, such as "Introduce Youself", "Luna Please send whatsapp message", "Tell me about your updates", "Start your Vision" Luna will process your query and perform the requested action or provide a response.

# Installation

1. Clone the repository
   ```bash
   git clone https://github.com/GitCoder052023/Luna.git
   ```

2. Install required libraries
   ```bash
   npm install
   ```
# Updates in Luna
## Update 1.1
Luna has been updated with a new text model called LunaTXT. This new model will make chatting with Luna even more enjoyable and engaging than before! 😍

With LunaTXT, you can now chat with Luna with complete privacy in public places. This new model has been added to ensure that your conversations with Luna are always secure and confidential. 🔒

So what are you waiting for? Start chatting with Luna today and experience the magic of LunaTXT! 🌟

## Update 1.2
**Luna’s Vision Capabilities: The Biggest Update Release Yet!**

We’re thrilled to announce that Luna, our AI-powered assistant, has been updated with vision capabilities. With this latest update, Luna can now see things and answer questions. This means you can now enjoy Luna’s vision capabilities to solve your homework questions, recognize things, and much more.

So what are you waiting for? Try out Luna’s vision capabilities today and see the difference for yourself!

Please note that Luna’s vision capabilities are still in beta, and we’re constantly working to improve them. If you have any feedback or suggestions, please don’t hesitate to reach out to me.

# Note
**Luna is currently under development, so expect some limitations and potential errors.
For more information on specific functions or modules, refer to the code documentation within those files**
