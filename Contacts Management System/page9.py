from os import name
from tkinter import *
import tkinter as tk
from tokenize import Name
import mysql.connector
def dbconnect():
    global mydb
    mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
    global mycursor
    mycursor = mydb.cursor()
def btn_clicked():
    dbconnect()
    root = Toplevel()
    text = Text(root) 
    name = nam.get()     
    mycursor.reset()
    mycursor.execute("call find_contact(%s)",(name,))
    result = mycursor.fetchall()
    try:
            text.insert(END,"Phone number:"+" "*(3)+"Name:\n")
            for i in result:
                st =""
                for j in i:
                    st+=str(j)+' '*2+'|'
                st+="\n"
                text.insert(END,st)
                text.pack()
            
    except:
        text.insert(END,"\n\n\n"+"*"*20+"No Contacts under that name"+"*"*20)
        text.pack()
    mydb.close()

def execute(ph):
    dbconnect()
    window = Tk()
    global nam
    nam = tk.StringVar()
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

    background_img = PhotoImage(file = f"9background.png")
    background = canvas.create_image(
        169.5, 73.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"9img_textBox0.png")
    entry0_bg = canvas.create_image(
        119.0, 183.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=nam,
        highlightthickness = 0)

    entry0.place(
        x = 37.0, y = 169,
        width = 164.0,
        height = 28)

    img0 = PhotoImage(file = f"9img0.png")
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
    mycursor.execute("select u_name from users where phone = concats(%s,'+91 ');",(ph,))
    result = mycursor.fetchone()
    canvas.create_text(
        145.0, 51.5,
        text = result[0],
        fill = "#000000",
        font = ("Tillana-Regular", int(15.0)))

    window.resizable(False, False)
    window.mainloop()
