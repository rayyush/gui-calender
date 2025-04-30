from tkinter import *
import calendar

def Calender_See():
    pass

if __name__ == '__main__':
    root = Tk() 
    root.config(background="red")
    root.title("GUI Calender")
    root.geometry("250x180")

    name = Label(root, text="Calendar", bg="Light green", font=("Arial", 20, "bold")) 
    name.grid(row=1, column = 1)

    root.mainloop()