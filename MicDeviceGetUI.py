

import customtkinter as ctk
import speech_recognition as sr
from PIL import Image, ImageTk
import threading
import settings
from settings import *

devices = sr.Microphone.list_microphone_names()

def device_select(device):
    for i, devicee in enumerate(devices):
        if(device == devicee):
            settings.selected_device_index["Selected Device Index"] = i

def Get_Device_Thread():
    tl = threading.Thread(target=Get_Device, args=())
    tl.start()

def Get_Device():
    # Get a list of available audio input devices

    speechtotext = ctk.CTkToplevel()
    speechtotext.geometry("250x100")
    speechtotext.title("Select Input")
    speechtotext.resizable(False, False)


    combobox = ctk.CTkOptionMenu(master=speechtotext,values=devices,command=device_select)
    combobox.pack(padx=20, pady=10)
    combobox.set(devices[0])

    green_tick_original = Image.open("green_tick.png")
    green_tick_resize = green_tick_original.resize((30, 30))
    green_tick = ImageTk.PhotoImage(green_tick_resize)

    done_button = ctk.CTkButton(master=speechtotext,corner_radius=10,command= lambda: speechtotext.destroy() , image=green_tick, text="",fg_color="White",hover_color="#EFF7ED",
                            width=30, height=30)
    done_button.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)


    speechtotext.mainloop()




