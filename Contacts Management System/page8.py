from tkinter import *
import tkinter as tk
import mysql.connector
def execute(pho):
        root = Tk()
        mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
        mycursor = mydb.cursor()
        mycursor.reset()
        mycursor.execute("call display_global_repo()")
        text = Text(root)            
        result = mycursor.fetchall()
        try:
            text.insert(END,"Phone Number"+" "*(len(result[0][0])-3)+"Name:\n")
            if(bool(result)):
                for i in result:
                    st =""
                    for j in i:
                        st+=str(j)+' '*2+'|'
                    st+="\n"
                    text.insert(END,st)
                    text.pack()
        except:
            text.insert(END,"\n\n\n"+"*"*20+"No contacts in the national repository"+"*"*20)
            text.pack()
        root.mainloop()