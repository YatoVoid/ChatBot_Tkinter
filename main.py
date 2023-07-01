from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import chatbotsetupfriendly2 as chatbotsetup
import threading
import texttospeech
from voice_to_text import *


# Window
root = ctk.CTk()
root.geometry("350x500")
root.title("V1Bot")
root.resizable(False, False)
ctk.set_appearance_mode("Light")

send_image_original = Image.open("send-message.png")  # Adding and resizing image for button
send_resize = send_image_original.resize((50, 50))
send_image = ImageTk.PhotoImage(send_resize)


settings_image_original = Image.open("settings.png")
image_resize = settings_image_original.resize((20, 20))
settings_image = ImageTk.PhotoImage(image_resize)

mic_image_original = Image.open("mic_image.png")
mic_resize = mic_image_original.resize((18, 18))
mic_image = ImageTk.PhotoImage(mic_resize)



def input_response(response):
    global label_gif

    try:
        # Create a message bubble frame
        responsetmp = response
        response = ""
        count = 1

        for i in responsetmp:
            if i == " " or i == "\t" or i == "\n":
                count += 1
            if (count % 5 == 0):
                response += "\n"
                count = 1
            response += i

    except("ServiceUnavailableError"):
        response = "Sorry Woli's Server is overloaded, wait abit"

    if label_gif:
        label_gif.pack_forget()  # Remove the label from the frame
        label = None


    bubble_frame = ctk.CTkFrame(frame, width=250, corner_radius=20, fg_color="lightblue")
    bubble_frame.pack(anchor="w", padx=0, pady=5)  # Adjust the padx and pady values as needed

    # Create a label inside the bubble frame
    label = ctk.CTkLabel(bubble_frame, text_color="Black", text=response, font=("Helvetica", 15), bg_color="lightblue")
    label.pack(expand=True, fill="both", padx=1, pady=5)


    frame.after(10, frame._parent_canvas.yview_moveto, 1.0)





def Text_To_Speech(response):
    texttospeech.read_text(response)

def Text_To_Speech_Thread(func,args):
    tc = threading.Thread(target=func, args=args)
    tc.start()

def background(message):
    response = chatbotsetup.Chat_Ressponse(message)
    if(settings_sheet["Text To Speech"]=="on"):
        Text_To_Speech_Thread(Text_To_Speech, (response,))


    input_response(response)

def Response_Gen(func,args):
    th = threading.Thread(target=func, args=args)
    th.start()

def Animation_Background(func,args):
    tb = threading.Thread(target=func, args=args)
    tb.start()

def background_anim():
    global label_gif
    # Load the animated GIF
    gif_path = "output-onlinegiftools.gif"
    gif = Image.open(gif_path)

    # Create a label and display the animated GIF
    label_gif = ctk.CTkLabel(frame)
    label_gif.pack()

    def update_label(index):
        # Seek the frame in the original GIF
        gif.seek(index)

        # Resize the frame
        resized_frame = gif.resize((150, 200))

        # Convert the resized frame to Tkinter-compatible image
        image = ImageTk.PhotoImage(resized_frame)
        label_gif.configure(image=image,text="")
        label_gif.image = image

        # Schedule the next frame update
        root.after(100, update_label, (index + 1) % gif.n_frames)

    # Start the animation
    frame.after(10, frame._parent_canvas.yview_moveto, 1.0)

    update_label(0)


def Send_Message(message=""):  # Button send function
    if message=="":
        count = 1
        messagetmp=entry.get()
        for i in messagetmp:
            if i == " " or i == "\t" or i == "\n":
                count+=1
            if(count%5==0):
                message += "\n"
                count = 1
            message+=i


    # Create a message bubble frame
    bubble_frame = ctk.CTkFrame(frame, width=250, corner_radius=20, fg_color="lightblue")
    bubble_frame.pack(anchor="e", padx=10, pady=5)  # Adjust the padx and pady values as needed

    # Create a label inside the bubble frame
    label = ctk.CTkLabel(bubble_frame, text_color="Black", text=message, font=("Helvetica", 15), bg_color="lightblue")
    label.pack(expand=True, fill="both", padx=10, pady=5)
    frame.after(10, frame._parent_canvas.yview_moveto, 1.0)

    entry.delete(0, "end")
    Animation_Background(background_anim, ())

    Response_Gen(background, (message,))
    #remove # to get response --------------------------------------------------------------------------------------------------------
    #response

#fix speech to text thread make it fucking work
def Send_Message_Without_Reply(message=""):
    if message=="":
        count = 1
        messagetmp=entry.get()
        for i in messagetmp:
            if i == " " or i == "\t" or i == "\n":
                count+=1
            if(count%5==0):
                message += "\n"
                count = 1
            message+=i
    # Create a message bubble frame
    bubble_frame = ctk.CTkFrame(frame, width=250, corner_radius=20, fg_color="lightblue")
    bubble_frame.pack(anchor="e", padx=10, pady=5)  # Adjust the padx and pady values as needed

    # Create a label inside the bubble frame
    label = ctk.CTkLabel(bubble_frame, text_color="Black", text=message, font=("Helvetica", 15), bg_color="lightblue")
    label.pack(expand=True, fill="both", padx=10, pady=5)
    frame.after(10, frame._parent_canvas.yview_moveto, 1.0)

    entry.delete(0, "end")




def Speech_To_Text():

    count = 1
    message = ""
    messagetmp = Voice_To_Text_Start()
    for i in messagetmp:
        if i == " " or i == "\t" or i == "\n":
            count += 1
        if (count % 5 == 0):
            message += "\n"
            count = 1
        message += i
    settings_sheet["Speech To Text"]="on"
    voice_record.configure(fg_color="green")
    if message=="Could not understand audio." or message=="Could not request results":
        Send_Message_Without_Reply(message)
    else:
        Send_Message(message)

def Speech_To_Text_Thread(func,args):
    if settings_sheet["Speech To Text"]=="on":
        settings_sheet["Speech To Text"]="recording"
        voice_record.configure(fg_color="red")
        tc = threading.Thread(target=func, args=args)
        tc.start()




def Settings():
    Settings_window_open()

def Settings_Thread(func,args):
    tp = threading.Thread(target=func, args=args)
    tp.start()



send = ctk.CTkButton(master=root, corner_radius=10, command=Send_Message, image=send_image, text="", fg_color="Blue",
                     width=30, height=40)
send.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

frame = ctk.CTkScrollableFrame(master=root, width=300, height=350, corner_radius=10, fg_color="White")
frame.place(relx=0.5, rely=0.43, anchor=tk.CENTER)

entry = ctk.CTkEntry(master=root, width=200, height=50, corner_radius=10)
entry.place(relx=0.4, rely=0.9, anchor=tk.CENTER)



voice_record = ctk.CTkButton(master=root, corner_radius=10, command=lambda :Speech_To_Text_Thread(Speech_To_Text, ()), text="", fg_color="Gray",
                     width=20, height=20, image=mic_image)

voice_record.place(relx=0.23, rely=0.03, anchor=tk.CENTER)

setting = ctk.CTkButton(master=root,corner_radius=10,command= lambda: Settings_Thread(Settings, ()), image=settings_image, text="",fg_color="Gray",
                        width=20, height=20)
setting.place(relx=0.1, rely=0.03, anchor=tk.CENTER)

def update_thread():
    tg = threading.Thread(target=update, args=())
    tg.start()

def update():
    if (settings_sheet["Speech To Text"] == "on"):
        voice_record.configure(fg_color="green")

    elif (settings_sheet["Speech To Text"]== "off"):
        voice_record.configure(fg_color="gray")



    root.after(5000, update)

root.after(0, update_thread())


def on_enter_key(event):
    Send_Message()


entry.bind("<Return>", on_enter_key)
root.mainloop()
