from tkinter import *
import tkinter.messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase1"
)
mycur = mydb.cursor()
#mycur.execute("CREATE DATABASE mydatabase1")
#mycur.execute("CREATE TABLE logindetails(id Integer PRIMARY KEY AUTO_INCREMENT,username VARCHAR(255),password VARCHAR(255))")

class Login:
    global Login
    def __init__(self):
        self.loginWindow = Tk()
        self.loginWindow.title("login")
        self.loginWindow.geometry("300x300")
        self.label1 = Label(self.loginWindow, text="Login Details",font="times 14 bold")
        self.label1.place(x=80,y=40)
        self.label2 = Label(self.loginWindow, text="Username",font="times 13 bold")
        self.label2.place(x=80,y=70)
        self.label3 = Label(self.loginWindow, text="Password",font="times 13 bold")
        self.label3.place(x=80,y=120)
        self.e1 = Entry(self.loginWindow)
        self.e1.place(x=80, y=100)
        self.e2 = Entry(self.loginWindow)
        self.e2.place(x=80, y=140)
        self.button1 = Button(self.loginWindow,text="Login", font="times 13 bold")
        self.button1.place(x=90, y=170)
        self.button2 = Button(self.loginWindow, text="Forgot password", font="times 10")
        self.button2.place(x=90,y=220)

    def run(self):
        self.loginWindow.mainloop()

class Register:
    def __init__(self):
        self.registerWindow = Tk()
        self.registerWindow.title("Register")
        self.registerWindow.geometry("300x300")
        self.label1 = Label(self.registerWindow, text="Register", font="times 15 bold")
        self.label1.place(x=80,y=40)
        self.label2 = Label(self.registerWindow, text="Username", font="times 15 bold")
        self.label2.place(x=80,y=80)
        self.username_ent = Entry(self.registerWindow)
        self.username_ent.place(x=80, y=110)
        self.label3 = Label(self.registerWindow, text="Password", font="times 15 bold")
        self.label3.place(x=80,y=130)
        self.pass_ent = Entry(self.registerWindow, show='*')
        self.pass_ent.place(x=80, y=160)
        self.button1 = Button(self.registerWindow, text="Register",font="times 13 bold",command=self.addUser)
        self.button1.place(x=90, y=190)

    def addUser(self):
        self.username = self.username_ent.get()
        self.password = self.pass_ent.get()

        if self.username =="":
            tkinter.messagebox.showinfo("warning","please fill info")
    def run(self):
        self.registerWindow.mainloop()