from tkinter import *
from login import Login,Register

class welcomeWin:
    def __init__(self):
        self.window = Tk()
        self.window.title("Welcome")
        self.window.geometry("300x300")
        self.label1 = Label(self.window, text="WELCOME", font="times 15 bold")
        self.label1.place(x=80, y=40)
        self.button1 = Button(self.window, text="LOGIN", font="times 13 bold",command=login)
        self.button1.place(x=90,y=100)
        self.button2 = Button(self.window, text="REGISTER", font="times 13 bold", command=register)
        self.button2.place(x=90,y=150)
        self.button1 = Button(self.window, text="Forgot password", font="times 10")
        self.button1.place(x=90,y=200)
    def run(self):
        self.window.mainloop()
def login():
    loginWindow = Login()
    loginWindow.run()
def register():
    registerWindow= Register()
    registerWindow.run()

window = welcomeWin()
window.run()