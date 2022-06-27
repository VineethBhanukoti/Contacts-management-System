from tkinter import *
import tkinter as tk
import mysql.connector
from matplotlib.pyplot import get
def dbconnect():
    global mydb
    mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
    global mycursor
    mycursor = mydb.cursor()
def btn_clicked():
    dbconnect()
    root = Toplevel()
    text = Text(root)        
    to_ph=pho.get()
    mycursor.reset()
    mycursor.execute("call dis_spec_call_log(%s,%s)",(pho1,to_ph,))
    result = mycursor.fetchall()
    try:
            text.insert(END,"LID:"+" "*(len(str(result[0][0]))-3)+"From number:"+" "*(4)+"To number:"+" "*(7)+"Date"+" "*(9)+"Time"+" "*(7)+"Duration\n")
            for i in result:
                st =""
                for j in i:
                    st+=str(j)+' '*2+'|'
                st+="\n"
                text.insert(END,st)
                text.pack()
            
    except:
        if(pho1!=pho):
            text.insert(END,"\n\n\n"+"*"*20+"You have not placed any calls yet"+"*"*20)
            text.pack()
        else:
            text.insert(END,"\n\n\n"+"*"*20+"You Cannot call your own number"+"*"*20)
            text.pack()
    mydb.close()
def execute(ph):
    dbconnect()
    global pho1
    pho1=ph
    global windows
    windows = Tk()
    global pho
    pho = tk.StringVar()
    windows.geometry("339x633")
    windows.configure(bg = "#ffffff")
    canvas = Canvas(
        windows,
        bg = "#ffffff",
        height = 633,
        width = 339,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"4background3.png")
    background = canvas.create_image(
        169.5, 70.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"4img_textBox03.png")
    entry0_bg = canvas.create_image(
        119.0, 179.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable= pho,
        highlightthickness = 0)

    entry0.place(
        x = 37.0, y = 165,
        width = 164.0,
        height = 28)
    img0 = PhotoImage(file = f"4img03.png")
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

    windows.resizable(False, False)
    windows.mainloop()
