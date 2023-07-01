
import customtkinter as ctk
import MicDeviceGetUI
from MicDeviceGetUI import Get_Device_Thread


GREEN = "#89C67B"
RED = "#CC4040"

selected_device_index = {"Selected Device Index": 0}
settings_sheet = {"Text To Speech" : "off", "Speech To Text": "off"}



def show():
    print(settings_sheet)

def Settings_window_open():
    global settings_sheet


    settings = ctk.CTkToplevel()
    settings.geometry("350x500")
    settings.title("Settings")
    settings.resizable(False, False)

    switch_var_tts = ctk.StringVar(value=settings_sheet["Text To Speech"])

    def switch_event_tts():

        if(switch_var_tts.get()=="off"):
            settings_sheet["Text To Speech"] = "off"
            text_to_speech.configure(button_color=RED,button_hover_color="#DE5959")


        else:
            settings_sheet["Text To Speech"] = "on"
            text_to_speech.configure(button_color=GREEN,button_hover_color="#A3DC96")

        show()




    text_to_speech = ctk.CTkSwitch(master = settings, text="Text To Speech",font=("Helvetica", 15), fg_color=(RED), progress_color=GREEN,
                                   button_color=RED,button_hover_color="#DE5959", switch_width=90,switch_height=40,
                                   command=switch_event_tts,variable=switch_var_tts, onvalue="on", offvalue="off")

    if settings_sheet["Text To Speech"] == "off":
        text_to_speech.configure(button_color=RED, button_hover_color="#DE5959")

    else:
        text_to_speech.configure(button_color=GREEN, button_hover_color="#A3DC96")


    text_to_speech.place(x=80, y=50)


    #-------------------------------------------------------------------------

    switch_var_stt = ctk.StringVar(value=settings_sheet["Speech To Text"])

    def switch_event_stt():

        if (switch_var_stt.get() == "off"):
            settings_sheet["Speech To Text"] = "off"
            speech_to_text.configure(button_color=RED, button_hover_color="#DE5959")

        else:
            settings_sheet["Speech To Text"] = "on"
            speech_to_text.configure(button_color=GREEN, button_hover_color="#A3DC96")
            Get_Device_Thread()


        show()

    speech_to_text = ctk.CTkSwitch(master=settings, text="Speech To Text", font=("Helvetica", 15), fg_color=(RED),
                                   progress_color=GREEN,
                                   button_color=RED, button_hover_color="#DE5959", switch_width=90, switch_height=40,
                                   command=switch_event_stt, variable=switch_var_stt, onvalue="on", offvalue="off")

    if settings_sheet["Speech To Text"] == "off":
        speech_to_text.configure(button_color=RED, button_hover_color="#DE5959")

    else:
        speech_to_text.configure(button_color=GREEN, button_hover_color="#A3DC96")

    speech_to_text.place(x=80, y=150)





    settings.mainloop()

