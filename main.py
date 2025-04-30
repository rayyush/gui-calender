from tkinter import *
import calendar

def Calender_See():
    window = Tk()
    

if __name__ == '__main__':
    root = Tk() 
    root.config(background="red")
    root.title("GUI Calender")
    root.geometry("250x180")

    name = Label(root, text="Calendar", bg="light green", font=("Arial", 20, "bold")) 
    name.grid(row=1, column = 1)
    year = Label(root, text="Enter the year", bg="light blue", font=("Arial", 18, "bold"))
    year.grid(row = 2, column = 2)
    year_entry = Entry(root, font=("Arial", 15, "bold"))
    year_entry.grid(row = 3, column = 3)
    show_button = Button(root, text = "Show Calender!", fg = "black", bg = "white", font=("Arial", 20, "bold"), command=Calender_See)


    root.mainloop()