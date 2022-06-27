from tkinter import *
import tkinter as tk
import mysql.connector

def execute(pho):
            print("Entered 5")
            mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
            mycursor = mydb.cursor()
            mycursor.reset()
            root = Tk()
            mycursor.reset()
            mycursor.execute("call display_contacts(%s)",(pho,))
            text = Text(root)            
            result = mycursor.fetchall()
            try:
                    text.insert(END,"Number:"+" "*(len(result[0][0])-3)+"Name:"+" "*(len(result[0][1])-4)+"\n")
                    for i in result:
                        st =""
                        for j in i:
                            st+=str(j)+' '*2+'|'
                        st+="\n"
                        text.insert(END,st)
                    text.pack()
            except:
                text.insert(END,"\n\n\n"+"*"*20+"You have not saved any contacts yet"+"*"*20)
                text.pack()
            root.mainloop()