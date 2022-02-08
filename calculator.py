##
#   @File       calculator.py
#   @Author     Martin Studeny \n
#               Faculty of Information Technology \n
#               Brno University of Technology \n
#               xstude23@fit.vutbr.cz
#   @Brief      Mathematical library for calculator's operations
#   @Version    1.0 Final
#   @Date       14. 04. 2016 (created)\n
#               24. 04. 2016 (edited)
#
#   @Mainpage   Welcome to the project's documentation. 
#

#   @Defgroup   displ Display functions
#   @Brief      Functions working with display content

from mathpack import Maths

try: # for Python2
    from Tkinter import *
except ImportError: # for Python3
    from tkinter import *

calc = Maths()
number=0
new_num = True
in_calc = False
nmm = 0
numbers = []
operation = ""
evaled = False
pressed = False

##
#   Function cleares the display, deletes all content
#   @Brief       Clear display
#   @Ingroup    displ
def clear():
    txtDisplay.delete(0,END)
    global new_num
    global in_calc
    global numbers
    global operation
    global pressed

    pressed = False
    operation = ""
    pressed = False
    new_num = True
    calc.ans = 0
    in_calc = False
    numbers = []
    return


##
#   Function inserts operator
#   @Brief       Add operator
#   @Ingroup    displ
def set_operation(oper):
    global operation
    global in_calc
    global nmm
    global numbers
    global pressed

    if not pressed:
        return

    if in_calc and operation != oper:
        return
    elif operation == oper:
        nmm = float(nmm)
        numbers.append(nmm)
        txtDisplay.delete(0,END)
    else:
        operation = oper
        in_calc = True
        nmm = float(nmm)
        numbers.append(nmm)
        txtDisplay.delete(0,END)
    pressed = False

##
#   Function manages pressing numbers in GUI.
#   @Brief       Pressing numbers
#   @Ingroup    displ
def num_press(num):
    global new_num
    global nmm
    global pressed
    global displayed
    global evaled

    if evaled:
        evaled = False
        txtDisplay.delete(0,END)

    pressed = True
    displayed = txtDisplay.get()
    if len(displayed) >= 10:
        return
    pressed = str(num)     
    if new_num:
        displayed = pressed
        new_num = False
    else:
        displayed = txtDisplay.get()
        if displayed == "0" and pressed =="0":
            return
        if pressed == ".":
            if pressed in displayed:
                return
        displayed = displayed + pressed
    nmm = displayed
    display(displayed)

##
#   Function calls operations & gets result of the mathematical operation
#   @Beif       Calls operation
#
#   @Param[in] numbers Array of entered numbers
#   @Param[in] operation Required operation (+ - * / ! ** %)
#
#   @Return Result of the operation
def evaluation():
    global in_calc
    global numbers
    global operation
    global nmm
    global pressed
    global evaled
    global new_num

    if not pressed or operation == "":
        return 

    pressed = False
    in_calc = False
    nmm = float(nmm)
    numbers.append(nmm)
    if operation == "+":
        calc.add(numbers)
    elif operation == "-":
        calc.substract(numbers)
    elif operation == "*":
        calc.mult(numbers)
    elif operation == "/":
        calc.div(numbers[0], numbers[1])
    elif operation == "!":
        calc.factorial(number[0])
    elif operation == "**":
        calc.pow(int(numbers[0]), int(numbers[1]))
    elif operation == "%":
        calc.modulo(numbers[0], numbers[1])
    else: 
        return
    operation = ""
    if calc.ans == None:
        display("ERR")
    else:
        display(calc.ans)
    evaled = True
    new_num = True
    numbers = []

##
#   Function makes display showing text
#   @Beif       Displays text
#   @Ingroup    displ
def display(text):
   txtDisplay.delete(0,END)
   txtDisplay.insert(0,text) 

##
#   Function for calculating factorial
#   @Beif       Factorial
#   @Ingroup    displ
def factorial():
    global in_calc
    global numbers
    global nmm
    global pressed
    global evaled
    global displayed
    global new_num

    if in_calc or not pressed:
        return

    nmm = int(nmm)
    numbers.append(nmm)
    calc.factorial(numbers[0])
    if calc.ans == None:
        display("ERR")
    else:
        display(calc.ans)
    evaled = True
    new_num = True
    numbers = []

def negation():
    global nmm
    global pressed

    if not pressed:
        return

    displayed = txtDisplay.get()
    if displayed == "0":
        return
    nmm = -(float(displayed))
    display(nmm)   




root = Tk()
frame = Frame(root)
frame.pack()

root.geometry("235x384")

root.title("Calculator")

num1 = StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)

txtDisplay = Entry(frame,textvariable = num1, bd = 15, width=235, insertwidth = 1, font = 30, justify="right", bg="#CCCCE0")
txtDisplay.pack(side = TOP)

frame0 = Frame(root)
frame0.pack(side = TOP)

button1 = Button(frame0, padx = 16.1, pady = 16.1, width=1, bd = 2, text = "+", fg="black", bg = "grey", command=  lambda: set_operation("+"))
button1.pack(side = LEFT)
button2 = Button(frame0, padx = 16.1, pady = 16.1, width=1, bd = 2, text = "-", fg="black", bg = "grey", command=  lambda: set_operation("-") )
button2.pack(side = LEFT)
button5 = Button(frame0, padx = 16.1, pady = 16.1, width=1, bd = 2, text = "+/-", fg="black", bg = "grey", command=  negation)
button5.pack(side = LEFT)
button3 = Button(frame0, padx = 16.1, pady = 16.1, width=1, bd = 2, text = "*", fg="black", bg = "grey", command=  lambda: set_operation("*"))
button3.pack(side = LEFT)
button4 = Button(frame0, padx = 16.1, pady = 16.1, width=1, bd = 2, text = "/", fg="black", bg = "grey", command=  lambda: set_operation("/"))
button4.pack(side = LEFT)

frame1 = Frame(root)
frame1.pack (side = TOP)

button1 = Button(frame1, padx = 22, pady = 22, width=1, bd = 2, text = "7", fg="black", command = lambda: num_press(7))
button1.pack(side = LEFT)
button2 = Button(frame1, padx = 22, pady = 22, width=1, bd = 2, text = "8", fg="black", command = lambda: num_press(8))
button2.pack(side = LEFT)
button3 = Button(frame1, padx = 22, pady = 22, width=1, bd = 2, text = "9", fg="black", command = lambda: num_press(9))
button3.pack(side = LEFT)
button4 = Button(frame1, padx = 22, pady = 22, width=1, bd = 2, text = "mod", fg="black", bg = "grey", command=  lambda: set_operation("%"))
button4.pack(side = LEFT)

frame2 = Frame(root)
frame2.pack (side = TOP)

button1 = Button(frame2, padx = 22, pady = 22, width=1, bd = 2, text = "4", fg="black", command = lambda: num_press(4))
button1.pack(side = LEFT)
button2 = Button(frame2, padx = 22, pady = 22, width=1, bd = 2, text = "5", fg="black", command = lambda: num_press(5))
button2.pack(side = LEFT)
button3 = Button(frame2, padx = 22, pady = 22, width=1, bd = 2, text = "6", fg="black", command = lambda: num_press(6))
button3.pack(side = LEFT)
button4 = Button(frame2, padx = 22, pady = 22, width=1, bd = 2, text = "!", bg = "grey", fg="black", command =  factorial)
button4.pack(side = LEFT)

frame3 = Frame(root)
frame3.pack (side = TOP)

button1 = Button(frame3, padx = 22, pady = 22, width=1, bd = 2, text = "1", fg="black", command = lambda: num_press(1))
button1.pack(side = LEFT)
button2 = Button(frame3, padx = 22, pady = 22, width=1, bd = 2, text = "2", fg="black", command = lambda: num_press(2))
button2.pack(side = LEFT)
button3 = Button(frame3, padx = 22, pady = 22, width=1, bd = 2, text = "3", fg="black", command = lambda: num_press(3))
button3.pack(side = LEFT)
button4 = Button(frame3, padx = 22, pady = 22, width=1, bd = 2, text = "^", bg = "grey", fg="black", command=  lambda: set_operation("**"))
button4.pack(side = LEFT)

frame4 = Frame(root)
frame4.pack (side = TOP)

button1 = Button(frame4, padx = 22, pady = 22, width=1, bd = 2, text = "0", fg="black", command = lambda: num_press(0))
button1.pack(side = LEFT)
button2 = Button(frame4, padx = 22, pady = 22, width=1, bd = 2, text = ".", fg="black", command = lambda: num_press("."))
button2.pack(side = LEFT)
button3 = Button(frame4, padx = 22, pady = 22, width=1, bd = 2, text = "C", bg = "grey", fg="black", command = clear)
button3.pack(side = LEFT)
button4 = Button(frame4, padx = 22, pady = 22, width=1, bd = 2, text = "=", bg = "grey", fg="black", command =  lambda: evaluation())
button4.pack(side = LEFT)


root.mainloop()
