
from tkinter import *

win = Tk()
win.title("calculator")
win.geometry("515x365")

win.resizable(0, 0)
# function to update the input field when a button is clicked


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# function to clear the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")
# function to evaluate the expression and display the result

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

                     
expression = ""
input_text = StringVar()


input_frame=  Frame(win, width=515, height=50)
input_frame.pack(side=TOP)

input_field=Entry(input_frame, font=("arial", 18, "bold"), width=45, justify=RIGHT, textvariable=input_text)
input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

btns_frame = Frame(win, width=315, height=270)
btns_frame.pack()

# Buttons first row


clear = Button(btns_frame, text= "c", width= 38, height= 3, command= lambda : btn_clear()).grid(row=0,column=0 , columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text= "/", width= 10, height= 3,command= lambda: btn_click ("/")).grid(row=0,column= 3, padx=1, pady=1)

# Buttons second row
seven = Button(btns_frame, text= "7", width= 10, height= 3, command= lambda: btn_click (7) ).grid(row=1,column=0, padx=1, pady=1)
eight = Button(btns_frame, text= "8", width= 10, height= 3, command= lambda: btn_click (8)).grid(row=1,column=1, padx=1, pady=1)
nine = Button(btns_frame, text= "9", width= 10, height= 3, command= lambda: btn_click (9)).grid(row=1,column=2, padx=1, pady=1)
multiply = Button(btns_frame, text= "*", width= 10, height= 3, command= lambda: btn_click ("*")).grid(row=1,column=3, padx=1, pady=1)

# Buttons third row
four = Button(btns_frame, text= "4", width= 10, height= 3, command= lambda: btn_click (4)).grid(row=2,column=0, padx=1, pady=1)
five = Button(btns_frame, text= "5", width= 10, height= 3, command= lambda: btn_click (5)).grid(row=2,column=1, padx=1, pady=1)
six = Button(btns_frame, text= "6", width= 10, height= 3, command= lambda: btn_click (6)).grid(row=2,column=2, padx=1, pady=1)
minus = Button(btns_frame, text= "-", width= 10, height= 3, command= lambda: btn_click ("-")).grid(row=2,column=3, padx=1, pady=1)

# Buttons fourth row
one = Button(btns_frame, text= "1", width= 10, height= 3, command= lambda: btn_click (1)).grid(row=3,column=0, padx=1, pady=1)  
two = Button(btns_frame, text= "2", width= 10, height= 3, command= lambda: btn_click (2)).grid(row=3,column=1, padx=1, pady=1)  
three = Button(btns_frame, text= "3", width= 10, height= 3, command= lambda: btn_click (3)).grid(row=3,column=2, padx=1, pady=1)    
plus = Button(btns_frame, text= "+", width= 10, height= 3, command= lambda: btn_click ("+")).grid(row=3,column=3, padx=1, pady=1)

# Buttons fifth row
zero = Button(btns_frame, text= "0", width= 22, height= 3, command= lambda: btn_click (0)).grid(row=4,column=0, columnspan=2, padx=1, pady=1)   
dot = Button(btns_frame, text= ".", width= 10, height= 3, command= lambda: btn_click (".")).grid(row=4,column=2, padx=1, pady=1)  
equal = Button(btns_frame, text= "=", width= 10, height= 3, command = lambda : btn_equal()).grid(row=4,column=3, padx=1, pady=1)





win.mainloop()



