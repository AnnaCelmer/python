from tkinter import*


def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btn_clear_display():
    global operator
    operator = ""
    text_Input.set("")


def btn_Equals_Input():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input =StringVar()

txtDisplay = Entry(master=cal, font=('Helvetica', 20, 'bold'), textvariable=text_Input,
                   bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4, sticky=NSEW)
# .grid() method to display defined wigdet on your aplication screen
btn1 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="1",
              width=2, height=2, command=lambda: btn_click(1)).grid(row=1, column=0, sticky=NSEW)
btn2 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="2",
              width=2, height=2, command=lambda: btn_click(2)).grid(row=1, column=1, sticky=NSEW)
btn3 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="3",
              width=2, height=2, command=lambda: btn_click(3)).grid(row=1, column=2, sticky=NSEW)
btn_addition = Button(cal, padx=16, bd=8, fg="black", bg="SkyBlue1", font=('Helvetica', 20, 'bold'),
                      text="+", width=2, height=2,  command=lambda: btn_click("+")).grid(row=1, column=3, sticky=NSEW)
# ===================================================================================
btn4 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="4",
              width=2, height=2, command=lambda: btn_click(4)).grid(row=2, column=0, sticky=NSEW)
btn5 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="5",
              width=2, height=2, command=lambda: btn_click(5)).grid(row=2, column=1, sticky=NSEW)
btn6 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="6",
              width=2, height=2, command=lambda: btn_click(6)).grid(row=2, column=2, sticky=NSEW)
btn_subtraction = Button(cal, padx=16, bd=8, fg="black", bg="SkyBlue1", font=('Helvetica', 20, 'bold'),
                         text="-", width=2, height=2, command=lambda: btn_click("-")).grid(row=2, column=3, sticky=NSEW)
# ===================================================================================
btn7 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="7",
              width=2, height=2, command=lambda: btn_click(7)).grid(row=3, column=0, sticky=NSEW)
btn8 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="8",
              width=2, height=2, command=lambda: btn_click(8)).grid(row=3, column=1, sticky=NSEW)
btn9 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="9",
              width=2, height=2, command=lambda: btn_click(9)).grid(row=3, column=2, sticky=NSEW)
btn_multiplication = Button(cal, padx=16, bd=8, fg="black", bg="SkyBlue1", font=('Helvetica', 20, 'bold'),
                            text="x", width=2, height=2, command=lambda: btn_click("*")).grid(row=3, column=3, sticky=NSEW)
# ====================================================================================
btn0 = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="0",
              width=2, height=2, command=lambda: btn_click(0)).grid(row=4, column=0, sticky=NSEW)
btn_clear = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="C",
              width=2, height=2, command=btn_clear_display).grid(row=4, column=1, sticky=NSEW)
btn_equal = Button(cal, padx=16, bd=8, fg="black", font=('Helvetica', 20, 'bold'), text="=",
              width=2, height=2, command=btn_Equals_Input).grid(row=4, column=2, sticky=NSEW)
btn_division = Button(cal, padx=16, bd=8, fg="black", bg="SkyBlue1", font=('Helvetica', 20, 'bold'),
                      text="/", width=2, height=2, command=lambda: btn_click("/")).grid(row=4, column=3, sticky=NSEW)

cal.mainloop()
