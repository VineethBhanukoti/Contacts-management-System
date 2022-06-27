from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
def execute():
    wind = Tk()
    global ph
    ph = tk.StringVar()
    wind.geometry("339x633")
    wind.configure(bg = "#ffffff")
    canvas = Canvas(
            wind,
            bg = "#ffffff",
            height = 633,
            width = 339,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
    canvas.place(x = 0, y = 0)

    upload= Image.open("img1.jpg")
    image=ImageTk.PhotoImage(upload,master=canvas)
    label= Label(wind,image=image,height = 210, width =210)
    label.place(x=71,y=105)
    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
            179.0, 506.0,
            image = entry0_img)
    entry0 = Entry(
            bd = 0,
            bg = "#f4ecec",
            textvariable= ph,
            highlightthickness = 0)
    entry0.place(
            x = 57.0, y = 490,
            width = 244.0,
            height = 32)
    canvas.create_text(
            170.0, 455.5,
            text = "Enter your phone number",
            fill = "#000000",
            font = ("Tillana-Regular", int(15.0),"italic"))
    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = exec1,
            relief = "flat")
    b0.place(
            x = 97, y = 554,
            width = 145,
            height = 36)
    wind.resizable(False, False)
    wind.mainloop()

def exec1():
    mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
    mycursor = mydb.cursor()
    mycursor.execute("select phone_verify(%s)",(ph.get(),))
    result = mycursor.fetchone()
    if(result[0] is None):
            mycursor.reset()
            print("Registering Number as New User:\n\nPlease Enter the Information down below to the BEST OF YOUR KNOWLEDGE:\n")
            name = input("Enter your Name: ")
            loc = input("Enter your location: ")
            oper = input("Enter your operator: ")
            try:
                mycursor.execute("call add_user(%s,%s,%s,%s)",(ph,name,loc,oper,))
                input()
            except :
                print("Error in the entered invalid Phone number or invalid Operator:")
                input()
            mydb.commit()
            mydb.close()
execute()