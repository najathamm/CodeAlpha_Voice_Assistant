# Voice Assistant

A simple voice assistant built using Python that can recognize speech commands and perform tasks like opening YouTube, searching Google, and playing music on Spotify.

## Features
- Recognizes voice commands using speech_recognition
- Converts text to speech with pyttsx3
- Opens YouTube, Spotify, and performs Google searches
- Handles errors gracefully 

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Install Required Libraries
Run the following command to install dependencies:

pip install speechrecognition pyttsx3 pyaudio

Note: If you encounter issues with pyaudio install it using:
- Windows: pip install pipwin && pipwin install pyaudio
- macOS: brew install portaudio && pip install pyaudio

## Usage
Run the script with:

python VoiceAssistant.py

Once running, say a command like:
- Open YouTube – Opens the YouTube homepage
- Search YouTube for Python tutorials – Searches for Python tutorials on YouTube
- Open Spotify – Opens Spotify
- Exit" or "Quit – Stops the assistant



