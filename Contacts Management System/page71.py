from tkinter import *
import tkinter as tk
import mysql.connector
import page7
import mysql.connector
def dbconnect():
    global mydb
    mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
    global mycursor
    mycursor = mydb.cursor()
def btn_clicked():
    window.destroy()
    dbconnect()
    mycursor.reset()
    mycursor.execute("select phone_verify(%s)",(pho.get(),))
    result = mycursor.fetchone()
    if(not result[0] is None):
        mydb.close()
        page7.execute(pho.get(),phos1)
    else:
        print("\n\n\n"+"*"*20+"The contact is not registered in the database"+"*"*20)

def execute(phos):
    dbconnect()
    global phos1
    phos1=phos
    global window
    window = Tk()
    global pho
    pho=tk.StringVar()
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

    background_img = PhotoImage(file = f"71background.png")
    background = canvas.create_image(
        169.5, 73.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"71img_textBox0.png")
    entry0_bg = canvas.create_image(
        119.0, 189.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=pho,
        highlightthickness = 0)

    entry0.place(
        x = 37.0, y = 175,
        width = 164.0,
        height = 28)

    img0 = PhotoImage(file = f"71img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 206, y = 550,
        width = 125,
        height = 46)
    mycursor.execute("select u_name from users where phone = concats(%s,'+91 ');",(phos1,))
    result = mycursor.fetchone()
    canvas.create_text(
        145.0, 51.5,
        text = result[0],
        fill = "#000000",
        font = ("Tillana-Regular", int(15.0)))

    window.resizable(False, False)
    window.mainloop()