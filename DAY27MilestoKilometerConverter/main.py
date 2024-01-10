from tkinter import *
window = Tk()

window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(pady=20, padx=20)


def miles_to_kilo():
    miles = float(miles_input.get())
    km = round(miles*1.609)
    kilometer_result_label.config(text=f"{km}")


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text="is_equal_to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)
kilometer_label.config(padx=10, pady=10)

calculate_button = Button(text="calculate", command=miles_to_kilo)
calculate_button.grid(column=1, row=2)




window.mainloop()