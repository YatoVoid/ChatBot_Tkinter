

import speech_recognition as sr
from settings import *


def Voice_To_Text_Start():

    print(selected_device_index["Selected Device Index"])
    text = ""
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=selected_device_index["Selected Device Index"])
    # Test the microphone
    with mic as source:
        print("Testing the microphone...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print("Recording finished. Recognizing speech...")
    try:
        text = r.recognize_google(audio)
        print("Recognized speech:", text)
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError as e:
        return "Could not request results"
    return text