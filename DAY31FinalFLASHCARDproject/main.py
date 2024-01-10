from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("C:\Desktop\Downloads/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(1000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def remove_word():
    to_learn.remove(current_card)
    remaining_words = pandas.DataFrame(to_learn)
    remaining_words.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("flashy")
window.minsize(width=1000, height=800)
window.config(pady=40, padx=80, bg=BACKGROUND_COLOR)
flip_timer = window.after(1000, func=flip_card)

canvas = Canvas(width=820, height=526)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(420, 273, image=card_front_img)
card_title = canvas.create_text(420, 100, text="", font=("ariel", 20, "italic"))
card_word = canvas.create_text(420, 240, text="", font=("ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="wrong.png")
unknown_word = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_word.grid(row=1, column=1)

check_image = PhotoImage(file="right.png")
known_word = Button(image=check_image, highlightthickness=0, command=remove_word)
known_word.grid(row=1, column=0)

next_card()
window.mainloop()
