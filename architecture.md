# Project Luna Architecture Overview

This document provides an overview of the architecture for the project Luna, detailing the purpose and functionality of each file. The project is structured to facilitate various functionalities, including message sending, query processing, operating system interactions, text-based interactions, vision processing, news fetching, scheduling tasks, audio processing, and weather information retrieval.

## Core Files

- **main.py**: Serves as the entry point of the application. It initializes the application and orchestrates the flow between different functionalities.

## Functionality Modules

- **SendWhatMessage.py**: Handles the automation of sending messages through WhatsApp. It includes functions to connect to WhatsApp Web, identify contacts, and send messages programmatically.

- **process_query.py**: Processes user queries by parsing input and determining the appropriate action or response. It acts as a bridge between the user input and the application's functionalities.

- **os_functions.py**: Contains utility functions for interacting with the operating system. This includes file manipulation, directory navigation, and executing system commands.

- **TextBasedLuna.py**: Manages text-based interactions, possibly serving as a chatbot or command interpreter for text inputs.

- **Vision.py**: Implements image processing and computer vision functionalities. It may include features such as object detection, image analysis, and visual data interpretation.

- **news.py**: Fetches and processes news from various sources. It could aggregate news, filter by topics, or provide summaries.

- **scheduler.py**: Manages scheduled tasks within the application. It allows for the execution of tasks at predefined times or intervals.

- **audio_processing.py**: Handles audio data processing, including recording, playback, and analysis of audio files.

- **dicts.py**: Likely contains dictionaries or mappings used throughout the application. This could include configuration settings, predefined responses, or data mappings.

- **Weather.py**: Provides functionalities related to weather information retrieval. This may include fetching current weather conditions, forecasts, and weather-related news.

## Visual Representation of Project structure

```Bash
C:.
│   .env
│   .gitattributes
│   .gitignore
│   .google-cookie
│   architecture.md
│   CODE_OF_CONDUCT.md
│   CONTRIBUTING.md
│   examples.md
│   License.md
│   output.txt
│   qodana.yaml
│   README.md
│   requirements.txt
│   todos.txt
│   
├───.GUI
│   │   main.py
├───.TUI
│   │   main.py
│                   
├───agents
│       main.py
│       
├───assets
│       logo.ico
│       logo.jpeg
│       qodana.yaml
│       
├───core
│   │   main.py
│   │   
│   └───core_utils
│           audio_processing.py
│           AutomateFuctions.py
│           dicts.py
│           news.py
│           os_functions.py
│           process_query.py
│           scheduler.py
│           SendWhatMessage.py
│           TextBasedLuna.py
│           Vision.py
│           Weather.py
│           
├───Installers - (BETA)
│       Luna - BETA.exe
│       
├───models
│   ├───locals
│   │   │   Luna.py
│   │           
│   └───Ollama
│       ├───large_models
│       ├───medium_models
│       │   ├───llama
│       │   │   ├───codellama
│       │   │   │       codellama.py
│       │   │   │       codellama34b.py
│       │   │   │       codellama70b.py
│       │   │   │       
│       │   │   └───llama2
│       │   │       │   llama2.py
│       │   │       │   llama2_70b.py
│       │   │       │   
│       │   │       └───__pycache__
│       │   │               llama2.cpython-310.pyc
│       │   │               llama2_70b.cpython-310.pyc
│       │   │               
│       │   └───mistral
│       │       │   mistral.py
│       │       │   
│       │       └───__pycache__
│       │               mistral.cpython-310.pyc
│       │               
│       └───small_models
│           ├───gemma_models
│           │   │   gemma.py
│           │   │   gemma2b.py
│           │   │   gemma7b.py
│           │   │   
│           │   └───__pycache__
│           │           gemma.cpython-310.pyc
│           │           gemma2b.cpython-310.pyc
│           │           gemma7b.cpython-310.pyc
│           │           
│           └───llama_models
│               ├───codellama
│               │       codellama13b.py
│               │       codellama7b.py
│               │       
│               └───llama2
│                       llama2_13b.py
│                       llama2_7b.py
│                       
├───utils
│   │   audio_processing.py
│   │   AutomateFuctions.py
│   │   dicts.py
│   │   news.py
│   │   os_functions.py
│   │   process_query.py
│   │   Weather.py

```