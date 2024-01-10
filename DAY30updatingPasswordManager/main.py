from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
               "S", "T", "V", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "$", "&", "?", "*", "@", "^", "#"]

    # print("welcome to the password generator! ")
    num_letters = random.randint(4, 6)
    num_numbers = random.randint(2, 4)
    num_symbols = random.randint(2, 4)
    pass_let = [random.choice(letters) for let in range(num_letters)]
    pass_num = [random.choice(numbers) for num in range(num_numbers)]
    pass_sym = [random.choice(symbols) for sym in range(num_symbols)]
    password_list = pass_let + pass_num + pass_sym
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="pls make sure you haven't left any field empty")
    else:
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)
                # data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as datafile:
                json.dump(new_data, datafile, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as datafile:
                json.dump(data, datafile, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    # is_ok = messagebox.askokcancel(title=website,
    #                                message=(f" Email: {email}\n Password: {password}\n Press ok to save or "
    #                                         f"cancel to update"))
    # if is_ok:
    # with open("data.txt", "a") as data_file:


#         #     data_file.write(f"{website} | {email} | {password}\n")
#         #     website_entry.delete(0, END)
#         #     password_entry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Such Datafile Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=70)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "njnrjpt@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=50)
password_entry.grid(row=3, column=1)

add_button = Button(width=60, height=1, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)
generate_pass = Button(width=15, height=1, text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()