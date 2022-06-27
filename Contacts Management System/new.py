from doctest import master
from tkinter import *
import tkinter as tk
from turtle import right
from PIL import Image, ImageTk
from asyncio import sleep
from asyncio.windows_events import NULL
from random import choice
from time import time
from datetime import datetime
from typing import final
from click import command
import mysql.connector
import page2
import page3
import page4
import page5
import page6
import page71
import page8
import page9
from os import system
while(True):
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
        command = wind.destroy,
        relief = "flat")

    b0.place(
        x = 97, y = 554,
        width = 145,
        height = 36)

    wind.resizable(False, False)
    wind.mainloop()
    mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
    mycursor = mydb.cursor()
    mycursor.execute("select phone_verify(%s)",(ph.get(),))
    result = mycursor.fetchone()
    if(result[0] is None):
       page2.execute() 
            
    else:
        while(True):
            winds = Tk()
            global choi
            choi = tk.StringVar()
            choi.set("To Display")
            mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
            mycursor = mydb.cursor()
            mycursor.execute("select u_name from users where phone = concats(%s,'+91 ');",(ph.get(),))
            result = mycursor.fetchone()
            winds.geometry("339x633")
            winds.configure(bg = "#ffffff")
            canvas = Canvas(
                winds,
                bg = "#ffffff",
                height = 633,
                width = 339,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)

            background_img = PhotoImage(file = f"background.png")
            background = canvas.create_image(
                169.5, 73.0,
                image=background_img)

            options = ["To Display all call logs till date","To Display call logs of specific number","To Display your contacts","To Add Contacts","To place a call","To Display National Repository",'To Find Contacts',"To Exit"]
            drop = OptionMenu( winds , choi , *options)
            drop.pack()
            drop.place(x = 37.0, y = 165,
                width = 164.0,
                height = 28)

            img0 = PhotoImage(file = f"img01.png")
            b0 = Button(
                image = img0,
                borderwidth = 0,
                command= winds.destroy,
                highlightthickness = 0,
                relief = "flat")

            b0.place(x = 206, y = 574,width = 125,height = 46)
            y = result[0]
            canvas.create_text(105.0, 51.5,text = y,fill = "#000000",font = ("Tillana-Regular", int(13.0)))
            winds.resizable(False, False)
            winds.mainloop()
            pho = ph.get()
            choic = choi.get()
            print(pho)
            print(choic)
            if(choic== "To Display all call logs till date"):
                page3.execute(pho)
            elif(choic=='To Display call logs of specific number'):
                print("Excuse me!!")
                page4.execute(pho)
            elif(choic == "To Display your contacts"):
                page5.execute(pho)
            elif(choic=="To Add Contacts"):
                page6.execute(pho)
            elif(choic == "To place a call" ):
                page71.execute(pho)
            elif(choic == "To Display National Repository"):
                page8.execute(pho)
            elif(choic == 'To Find Contacts'):
                page9.execute(pho)
            else:
                break