import tkinter as tk
from unicodedata import name
from matplotlib.cbook import to_filehandle
from tkinter import *
from tkinter import messagebox

# Import mysql.connector module to connect to the database
import mysql.connector


def btn_clicked():
    
    print("Button Clicked")
    print(pho.get())
    print(nam.get())
    print(oper.get())
    # if(not pho.get().isdigit() or len(pho.get())!=10 or oper.get() =="Select" ):
    #     messagebox.showerror("Error in the entered Data")
    if(True):
        try:
            mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
            mycursor = mydb.cursor()
            mycursor.execute("call add_user(%s,%s,%s,%s)",(pho.get(),nam.get(),loc.get(),oper.get(),))
            
            mydb.commit()
            mydb.close()
        except:
            messagebox.showerror("Error","Error in the Entered Data")
        window.destroy()

def execute():
    global window
    window = Tk()
    global pho
    pho = tk.StringVar()
    global loc
    loc = tk.StringVar()
    global nam
    nam = tk.StringVar()
    global oper
    oper = tk.StringVar()
    oper.set("Select")
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

    background_img = PhotoImage(file = f"2background.png")
    background = canvas.create_image(
        169.5, 198.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"2img_textBox0.png")
    entry0_bg = canvas.create_image(
        119.0, 200.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=pho,
        highlightthickness = 0)

    entry0.place(
        x = 37.0, y = 186,
        width = 164.0,
        height = 28)

    entry1_img = PhotoImage(file = f"2img_textBox1.png")
    entry1_bg = canvas.create_image(
        119.0, 279.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=loc,
        highlightthickness = 0)

    entry1.place(
        x = 37.0, y = 265,
        width = 164.0,
        height = 28)

    options = ["Vodophone Idea","Bharati Airtel","BSNL","JIO"] 
    drop = OptionMenu( window , oper , *options)
    drop.pack()

    drop.place(
        x = 37.0, y = 340,
        width = 164.0,
        height = 28)

    entry3_img = PhotoImage(file = f"2img_textBox3.png")
    entry3_bg = canvas.create_image(
        119.0, 433.0,
        image = entry3_img)

    entry3 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=nam,
        highlightthickness = 0)

    entry3.place(
        x = 37.0, y = 419,
        width = 164.0,
        height = 28)

    img0 = PhotoImage(file = f"2img0.png")
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

    window.resizable(False, False)
    window.mainloop()
