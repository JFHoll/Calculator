# Calculator

from tkinter import *

#Function to add any number or symbol button pressed to the calculation
def button(x, lbl2):
    global expression
    expression = (expression + str(x))
    input_text.set(expression)
    lbl2.configure(text=expression)

#Function to clear the calculation when the Clear button is pressed
def clear(lbl2):
    global expression
    expression = ""
    input_text.set(expression)
    lbl2.configure(text=expression)

#Function to calculate the answer
def equals():
    global expression
    #Debugging to catch any impossible calculations
    try:

        answer = str(eval(expression))
        input_text.set(answer)
        lbl2.configure(text=answer)

    except:

        lbl2.configure(text= "Error")

expression = ""

#Set up the window
window = Tk()
window.geometry("505x635")
window.resizable(False, False)

input_text = StringVar(expression)

#Set up the frame
frame = Frame(window)
frame.grid(row=2)

#Heading label
lbl1 = Label(text="Calculator", font=("Arial", 25))
lbl1.grid(row=0)

#Label to contain the calculation as the user presses buttons
lbl2 = Label(master=window, text="Your Calculation Here!", font=("Arial", 30), borderwidth=2, relief="solid", height="1", width="10")
lbl2.grid(row=1, sticky="we")

#Configuration for the calculator buttons
onebtn = Button(master=frame, text="1", font=("Arial", 40), bd=10, command=lambda: button(1, lbl2))
twobtn = Button(master=frame, text="2", font=("Arial", 40), bd=10, command=lambda: button(2, lbl2))
threebtn = Button(master=frame, text="3", font=("Arial", 40), bd=10, command=lambda: button(3, lbl2))
plusbtn = Button(master=frame, text="+", font=("Arial", 40), bd=10, command=lambda: button("+", lbl2))
minusbtn = Button(master=frame, text="-", font=("Arial", 40), bd=10, command=lambda: button("-", lbl2))

fourbtn = Button(master=frame, text="4", font=("Arial", 40), bd=10, command=lambda: button(4, lbl2))
fivebtn = Button(master=frame, text="5", font=("Arial", 40), bd=10, command=lambda: button(5, lbl2))
sixbtn = Button(master=frame, text="6", font=("Arial", 40), bd=10, command=lambda: button(6, lbl2))
multiplybtn = Button(master=frame, text="X", font=("Arial", 40), bd=10, command=lambda: button("*", lbl2))
dividebtn = Button(master=frame, text="/", font=("Arial", 40), bd=10, command=lambda: button("/", lbl2))

sevenbtn = Button(master=frame, text="7", font=("Arial", 40), bd=10, command=lambda: button(7, lbl2))
eightbtn = Button(master=frame, text="8", font=("Arial", 40), bd=10, command=lambda: button(8, lbl2))
ninebtn = Button(master=frame, text="9", font=("Arial", 40), bd=10, command=lambda: button(9, lbl2))
decimalbtn = Button(master=frame, text=".", font=("Arial", 40), bd=10, command=lambda: button(".", lbl2))

clearbtn = Button(master=frame, text="C", font=("Arial", 40), bd=10, command=lambda: clear(lbl2))
zerobtn = Button(master=frame, text="0", font=("Arial", 40), bd=10, command=lambda: button(0, lbl2))
equalsbtn = Button(master=frame, text="=", font=("Arial", 40), bd=10, command=lambda: equals())

#Positioning of calculator buttons
onebtn.grid(row=0, column=0, padx=5, pady=5)
twobtn.grid(row=0, column=1, padx=5, pady=5)
threebtn.grid(row=0, column=2, padx=5, pady=5)
plusbtn.grid(row=0, column=3, padx=5, pady=5)
minusbtn.grid(row=0, column=4, padx=5, pady=5)

fourbtn.grid(row=1, column=0, padx=5, pady=5)
fivebtn.grid(row=1, column=1, padx=5, pady=5)
sixbtn.grid(row=1, column=2, padx=5, pady=5)
multiplybtn.grid(row=1, column=3, padx=5, pady=5)
dividebtn.grid(row=1, column=4, padx=5, pady=5)

sevenbtn.grid(row=2, column=0, padx=5, pady=5)
eightbtn.grid(row=2, column=1, padx=5, pady=5)
ninebtn.grid(row=2, column=2, padx=5, pady=5)
decimalbtn.grid(row=2, column=3, columnspan=2, padx=5, pady=5, sticky="we")

clearbtn.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")
zerobtn.grid(row=3, column=2, padx=5, pady=5)
equalsbtn.grid(row=3, column=3, columnspan=2, padx=5, pady=5, sticky="we")

window.mainloop()
