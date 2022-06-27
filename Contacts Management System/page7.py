from tkinter import *
import tkinter as tk
import mysql.connector
from time import time
from datetime import datetime
import time
import datetime
import mysql.connector
def btn_clicked():
    window.destroy()
    mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
    mycursor = mydb.cursor()
    finaltime = datetime.datetime.now()
    duration = finaltime - now
    dates = str(now.year)+ "-" +str(now.month) + "-" + str(now.day)
    print(duration)
    print(dates)
    mycursor.execute("call add_call_his(%s,%s,%s,%s,%s)",(phos,pho_to,dates,now,duration))
    mydb.commit()

def execute(pho,phos1):
    global pho_to
    pho_to = pho
    global phos
    phos =phos1
    global window
    window = Tk()
    global now
    now = datetime.datetime.now()
    window.geometry("339x633")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 633,
        width = 339,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"7background.png")
    background = canvas.create_image(
        169.5, 316.5,
        image=background_img)

    img0 = PhotoImage(file = f"7img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 117, y = 517,
        width = 105,
        height = 109)

    canvas.create_text(
        86.5, 59.5,
        text = "Connected",
        fill = "#ffffff",
        font = ("Tillana-Regular", int(25.0)))

    canvas.create_text(
        107.0, 117.5,
        text = "+91 "+pho,
        fill = "#ffffff",
        font = ("Tillana-Regular", int(25.0)))

    window.resizable(False, False)
    window.mainloop()
