from tkinter import *


class Login:
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
        self.e1 = Entry(self.registerWindow)
        self.e1.place(x=80, y=110)
        self.label3 = Label(self.registerWindow, text="Password", font="times 15 bold")
        self.label3.place(x=80,y=130)
        self.e2 = Entry(self.registerWindow, show='*')
        self.e2.place(x=80, y=160)
        self.button1 = Button(self.registerWindow, text="Register",font="times 13 bold")
        self.button1.place(x=90, y=190)
    def run(self):
        self.registerWindow.mainloop()