
from tkinter import *

win = Tk()
win.title("calculator")
win.geometry("515x365")

win.resizable(0, 0)

input_frame=  Frame(win, width=515, height=50)
input_frame.pack(side=TOP)

input_field=Entry(input_frame, font=("arial", 18, "bold"), width=45, justify=RIGHT)
input_field.grid(row=0, column=0)








win.mainloop()



