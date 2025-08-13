import tkinter as tk

calculation=""
def add_to_calculation(symbol):
    global calculation
    calculation+= str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation= str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"ERROR")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

root= tk.Tk()
root.geometry("300x275")

text_result= tk.Text(root, height=2.5, width=25, font=("Arial", 16))
text_result.grid(columnspan=5)

Btn_1= tk.Button(root, text="1", command= lambda: add_to_calculation(1), width= 5, font= ("Arial", 16))
Btn_1.grid(column=1, row=2)

Btn_2= tk.Button(root, text="2", command= lambda: add_to_calculation(2), width= 5, font= ("Arial", 16))
Btn_2.grid(column=2, row=2)

Btn_3= tk.Button(root, text="3", command= lambda: add_to_calculation(3), width= 5, font= ("Arial", 16))
Btn_3.grid(column=3, row=2)

Btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 16))
Btn_4.grid(column=1, row=3)

Btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 16))
Btn_5.grid(column=2, row=3)

Btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 16))
Btn_6.grid(column=3, row=3)

Btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 16))
Btn_7.grid(column=1, row=4)

Btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 16))
Btn_8.grid(column=2, row=4)

Btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 16))
Btn_9.grid(column=3, row=4)

Btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 16))
Btn_0.grid(column=2, row=5)

Btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 16))
Btn_plus.grid(column=4, row=2)

Btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 16))
Btn_minus.grid(column=4, row=3)

Btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 16))
Btn_multiply.grid(column=4, row=4)

Btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 16))
Btn_div.grid(column=4, row=5)

Btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 16))
Btn_open.grid(column=1, row=5)

Btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 16))
Btn_close.grid(column=3, row=5)

Btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 16))
Btn_equals.grid(column=1, row=6,columnspan=2)

Btn_clear= tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 16))
Btn_clear.grid(column=3, row=6,columnspan=2)
root.mainloop()
