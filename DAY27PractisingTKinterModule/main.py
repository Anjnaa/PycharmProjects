"""tkinter windows and labeling"""

# import tkinter
# window = tkinter.Tk()
#
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
#
# my_label = tkinter.Label(text="I am a Label", font=("arial", "24", "bold"))
# my_label.pack(expand=True)
#
# my_label["text"] = "New Label"
# my_label.config(text="second new label")
#
# window.mainloop()

"""249. Many Positional arguments(*args)"""
# def add(*args):
#     print(args)
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(32,44,66,11,23,32,21,25))

"""250. **kwargs: Many keyword arguments"""

# def calculate(n, **kargs):
#     print(kargs)
#     for key,value in kargs.items():
#         print(key)
#         print(value)
#     n += kargs["add"]
#     n *= kargs["multiply"]
#     print(n)
# calculate(24, add=2, multiply=5)

# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs["make"]
#         self.model = kwargs.get("model")
#         self.color = kwargs.get("color")
#         self.seat = kwargs.get("seat")
#
# my_car = Car(make="Nissan India", model="GT-R")
# print(my_car.make)
# print(my_car.model)
# print(my_car.color)
# print(my_car.seat)


"""251. changing label using button"""
# from tkinter import *
#
# window = Tk()
# window.title("Changing Label Using Button")
# window.minsize(width=500, height=300)
# my_label = Label(text="I am a label", font=("arial", "20", "bold"))
# my_label.pack()
# def use_button():
#     print("I Got Clicked")
#     my_label.config(text="Button got clicked")
#     changing_text = enter_in.get()
#     my_label.config(text=changing_text)
# button = Button(text="ClickMe", font=("arial", "12", "bold"), command=use_button)
# button.pack()
#
# enter_in = Entry(width=20, highlightthickness=12 )
# enter_in.pack()
# print(enter_in.get())
#
# window.mainloop()

"""252. widgets,radiobuttons, checkbuttons, scales """

# from tkinter import *
#
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# my_label = Label()
# my_label.config(text="Button got clicked")
# my_label.pack()
#
#
# def use_button():
#     print("I Got Clicked")
#     changing_text = entery.get()
#     my_label.config(text=changing_text)
#
#
# button = Button(text="ClickMe", font=("arial", "12", "bold"), command=use_button)
# button.pack()
#
# entery = Entry(width=20, highlightthickness=12)
# entery.insert(END, string="some starting text")
# entery.get()
# entery.pack()
#
# text = Text(width=30, height=5)
# text.focus()
# text.insert(END, "examples of multiline entery")
# text.get("1.0")
# text.pack()
#
#
# def use_spinbox():
#     print(spinbox.get())
#
#
# spinbox = Spinbox(width=5, from_=0, to=10, command=use_spinbox)
# spinbox.pack()
#
#
# def use_scale(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=use_scale)
# scale.pack()
#
#
# def use_checkbutton():
#     print(checked.get())
#
#
# checked = IntVar()
# check_button = Checkbutton(text="on/off", variable=checked, command=use_checkbutton)
# check_button.pack()
#
#
# def use_radio():
#     print(radio_state.get())
#
#
# radio_state = IntVar()
# radiobutton_1 = Radiobutton(text="option_1", value=1, variable=radio_state, command=use_radio)
# radiobutton_1.pack()
#
# radiobutton_2 = Radiobutton(text="option_2", value=2, variable=radio_state, command=use_radio)
# radiobutton_2.pack()
#
#
# def using_listbox(event):
#     print(list_box.get(list_box.curselection()))
#
#
# list_box = Listbox(height=4)
# fruits = ["apple", "banana", "carrot", "drumsticks", "eggs", "fish"]
# for item in fruits:
#     list_box.insert(fruits.index(item), item)
#
# list_box.bind("<<ListboxSelect>>", using_listbox)
# list_box.pack()
#
# window.mainloop()

"""253. pack place grid"""

from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

my_label = Label()
my_label.config(text="Button got clicked")
my_label.grid(row=0, column=0 )
my_label.config(padx=20, pady=40)

button = Button(text="ClickMe", font=("arial", "12", "bold"))
button.grid(row=1, column=1)

entery = Entry(width=20, highlightthickness=12)
entery.insert(END, string="some starting text")
entery.get()
entery.grid(row=2, column=2)

text = Text(width=30, height=5)
text.focus()
text.insert(END, "examples of multiline entry")
text.get("1.0")
text.grid(row=3, column=3)

window.mainloop()


