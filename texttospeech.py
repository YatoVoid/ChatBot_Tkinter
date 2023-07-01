import pyttsx3
from settings import settings_sheet

# Initialize the pyttsx3 engine

engine = pyttsx3.init()


# Set the rate of speech
engine.setProperty('rate', 230)  # You can adjust the rate as needed

# Function to read text out loud
def read_text(text):

    engine.say(text)
    engine.runAndWait()

    # Clean up the engine
    engine.stop()
    settings_sheet["Current_tts"] = "off"




