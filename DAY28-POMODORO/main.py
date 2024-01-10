# import cv2
# print(cv2.__version__)
from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text="Timer")
    check_marks.config("text=")
    global reps
    reps = 0



# ---------------------------- TIME MECHANISM ------------------------------- #
def start_timer(title_label=None):
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(long_break_sec)
        title_label.config(text="Work", fg=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks = "✔"
        check_marks.config(text=marks)


window = Tk()
window.title("POMODORA")
# window.minsize(width=300, height=280)
window.config(padx=100, pady=50, background="purple")

timer_label = Label(text="Timer", fg="black", bg="white", font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

canvas = Canvas(height=200, width=230, background="yellow", highlightthickness=10)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 40,"bold"))
canvas.grid(column=1, row=1)
count_down(5)

start_button = Button(text="Start",highlightthickness=10, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=10, command=reset_timer)
reset_button.grid(column=2, row=2)


check_marks = Label(fg="green", bg="white")
check_marks.grid(column=1, row=2)

window.mainloop()
