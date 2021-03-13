import pyttsx3
from tkinter import *
import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.title("Speak")
root.iconbitmap("E:\Saini\Programming\Python\projects\speak\download.ico")
root.config(bg="blue")
root.geometry("600x400")

eng = pyttsx3.init("sapi5")
voices = eng.getProperty("voices")
eng.setProperty('voices',voices[1].id)
def speak(audio):
    eng.say(audio)
    eng.runAndWait()
ttk.Label(root,text="Write the sentences or word down in the box").pack(pady=10,side="top")
a=tk.StringVar()
ttk.Entry(root,width=40,text=a).pack(side="top",padx=100,pady=100)
def say():
    k=a.get()
    speak(k)
    ttk.Entry(root,text=a).delete(0,tk.END)
ttk.Button(root,width=15,text="Submit",command=say).pack(pady=30,padx=10)

root.mainloop()


    
