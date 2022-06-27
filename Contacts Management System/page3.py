from tkinter import *
import tkinter as tk
import mysql.connector
def execute(pho):
        root = Tk()
        mydb = mysql.connector.connect(host = 'localhost',user = 'root', passwd = '1234',database = 'cms')
        mycursor = mydb.cursor()
        mycursor.reset()
        mycursor.execute("CALL display_call_log(%s)",(pho,))
        text = Text(root)            
        result = mycursor.fetchall()
        try:
            text.insert(END,"Name:"+" "*(len(result[0][0])-3)+"To number:"+" "*(len(result[0][1])-7)+"Date"+" "*(len(str(result[0][2]))-1)+"Time"+" "*(len(str(result[0][3])))+"Duration\n")
            if(bool(result)):
                for i in result:
                    st =""
                    for j in i:
                        st+=str(j)+' '*2+'|'
                    st+="\n"
                    text.insert(END,st)
                    text.pack()
        except:
            text.insert(END,"\n\n\n"+"*"*20+"You have not placed any calls yet"+"*"*20)
            text.pack()
        root.mainloop()