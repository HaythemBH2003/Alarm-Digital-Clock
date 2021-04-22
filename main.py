import time
from tkinter import *
from pygame import mixer
import os
mixer.init()
mixer.music.load("sound.mp3")
screen = Tk()
screen.geometry("600x250")
screen.wm_attributes("-alpha", 0.5)
screen.title("                                                                           Digital Clock")
bg_image = PhotoImage(file="dragon.png")
alarm_image = PhotoImage(file="alarm button icon after cut.png")


def set_alarm():
    global hour_entry
    global minute_entry
    global hour
    global minute
    global LM
    global LH
    global confirm_alarm
    screen.geometry("600x400")
    alarm_button.config(state="disabled")
    hour = StringVar
    minute = StringVar
    LH = Label(text="Enter Alarm Hour :")
    LH.pack()
    hour_entry = Entry(textvariable=hour, justify="center")
    hour_entry.pack()
    LM = Label(text="Enter Alarm Minute :")
    LM.pack()
    minute_entry = Entry(textvariable=minute, justify="center")
    minute_entry.pack()
    confirm_alarm = Button(text="Confirm Alarm", bg="#318ce7", fg="white", bd="0", highlightthickness="0", height="1", command=confirming_alarm)
    confirm_alarm.pack()


def confirming_alarm():
    global alarm_hour
    global alarm_minute
    hour_entry.forget()
    minute_entry.forget()
    LM.forget()
    LH.forget()
    confirm_alarm.forget()
    screen.geometry("600x250")
    alarm_hour = hour_entry.get()
    alarm_minute = minute_entry.get()
    if alarm_hour != "" and alarm_minute != "":
        my_canvas.itemconfigure(alarm_label, text=("       Alarm: ON. At: "+str(alarm_hour)+":"+str(alarm_minute)))


def checking_alarm():
    global current_minute
    global current_hour
    global alarm_hour
    global alarm_minute
    try:
        if alarm_hour != "" and alarm_minute != "":
            mn = int(alarm_minute)
            hr = int(alarm_hour)
            #my_canvas.itemconfigure(alarm_label, text="Alarm : ON")
            current_hour = int(time.strftime("%H"))
            current_minute = int(time.strftime("%M"))
            if current_minute == mn and current_hour == hr and int(time.strftime("%S")) == 00:
                mixer.music.play()
                my_canvas.itemconfigure(alarm_label, text="Alarm : OFF")
                current_minute = ""
                current_hour = ""
    except:
        "name 'alarm_hour' is not defined"


checking_alarm()


def cancel_alarm():
    global alarm_hour
    global alarm_minute
    global current_minute
    global current_hour
    alarm_button.config(state="normal")
    alarm_hour = ""
    alarm_minute = ""
    my_canvas.itemconfigure(alarm_label, text="Alarm : OFF")
    mixer.music.stop()
    current_minute = ""
    current_hour = ""


def leave_app():
    screen.destroy()
    os.system("TASKKILL /F /IM clockalarm.exe")


my_canvas = Canvas(screen, width="600", height="250", bd=0, highlightthickness=0)
my_canvas.pack()
my_canvas.create_image(0, 0, image=bg_image, anchor="nw")
my_canvas.pack()
p = my_canvas.create_text(300, 125, text=StringVar, font=("Helvetica", 80), fill="grey100")
my_canvas.pack()
alarm_button = Button(image=alarm_image, bg="#318ce7", fg="grey80", bd="0", highlightthickness="0", command=set_alarm)
alarm_button.place(x=285, y=185)
cancel_alarm_button = Button(text="Cancel Alarm", bg="#318ce7", fg="grey80", bd="0", highlightthickness="0", height="1", command=cancel_alarm)
cancel_alarm_button.place(x=263, y=210)
exit_button = Button(text="Close Time App", bg="#318ce7", fg="grey80", bd="0", highlightthickness="0", height="1", command=leave_app)
exit_button.place(x=256, y=230)
alarm_label = my_canvas.create_text(50, 20, text="Alarm : OFF", font=("Helvetica", 10), fill="grey90")
my_canvas.pack()


def get_time():
    current_time = time.strftime("%H:%M:%S")
    checking_alarm()
    my_canvas.itemconfigure(p, text=current_time)
    my_canvas.after(1000, get_time)


get_time()
screen.mainloop()
