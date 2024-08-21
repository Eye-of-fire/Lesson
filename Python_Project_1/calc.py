import tkinter as tk

def get_values():
    num_1 = int(number_1_entry.get())
    num_2 = int(number_2_entry.get())
    return num_1, num_2

def get_value(value):
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, value)

def add():
    num_1 = int(number_1_entry.get())
    num_2 = int(number_2_entry.get())
    res = num_1 + num_2
    get_value(res)

def sub():
    num_1 = int(number_1_entry.get())
    num_2 = int(number_2_entry.get())
    res = num_1 - num_2
    get_value(res)

def mul():
    num_1 = int(number_1_entry.get())
    num_2 = int(number_2_entry.get())
    res = num_1 * num_2
    get_value(res)

def div():
    num_1 = int(number_1_entry.get())
    num_2 = int(number_2_entry.get())
    res = num_1 / num_2
    get_value(res)


window = tk.Tk()
window.title('Calculator')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window,text= '+',width=2,height=2, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window,text= '-',width=2,height=2,command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window,text= '*',width=2,height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window,text= '/',width=2,height=2, command=div)
button_div.place(x=250, y=200)
number_1_entry = tk.Entry(window,width=28)
number_1_entry.place(x=100, y=75)
number_2_entry = tk.Entry(window,width=28)
number_2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window,width=28)
answer_entry.place(x=100, y=300)
number_1 = tk.Label(window,text='введите первое число')
number_1.place(x=100, y=50)
number_2 = tk.Label(window,text='введите второе число')
number_2.place(x=100, y=120)
answer = tk.Label(window,text='ответ')
answer.place(x=100, y=270)

window.mainloop()