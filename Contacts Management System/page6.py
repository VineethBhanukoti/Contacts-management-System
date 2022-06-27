from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
def dbconnect():
    global mydb
    mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
    global mycursor
    mycursor = mydb.cursor()
def btn_clicked():
        dbconnect()
        mycursor.reset()
        root = Toplevel()
        text = Text(root) 
        name = nam.get()
        phone = phon.get()
        print(name)
        print(phone)
        print(ph)
        try:
            mycursor.execute("insert into contacts values(concats(%s,'+91 '),%s,concats(%s,'+91 '));",(phone,name,ph))
            messagebox.showinfo("Success","The contact is added successfully to your contacts")
        except:
            messagebox.showerror("Error","The Contact is not Registered")

        mydb.commit()
        mydb.close()

def execute(pho):
    dbconnect()
    global ph
    ph=pho
    window = Tk()
    global nam
    nam = tk.StringVar()
    global phon
    phon = tk.StringVar()
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

    background_img = PhotoImage(file = f"6background.png")
    background = canvas.create_image(
        169.5, 128.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"6img_textBox0.png")
    entry0_bg = canvas.create_image(
        119.0, 179.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=nam,
        highlightthickness = 0)

    entry0.place(
        x = 37.0, y = 165,
        width = 164.0,
        height = 28)

    entry1_img = PhotoImage(file = f"6img_textBox1.png")
    entry1_bg = canvas.create_image(
        119.0, 296.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=phon,
        highlightthickness = 0)

    entry1.place(
        x = 37.0, y = 282,
        width = 164.0,
        height = 28)

    img0 = PhotoImage(file = f"6img0.png")
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
