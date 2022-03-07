import tkinter as tk
from tkinter import messagebox, simpledialog
from random import choice, shuffle
from string import ascii_letters, digits
import pyperclip
# import pyperclip package, to copy the newly generated password to clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ascii_letters

numbers = digits
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():

    nr_letters = int(simpledialog.askstring(
        title="Password Generator", prompt="How many letters would you like in your password?"))

    nr_symbols = int(simpledialog.askstring(
        title="Password Generator", prompt="How many symbols would you like?"))
    nr_numbers = int(simpledialog.askstring(
        title="Password Generator", prompt="How many numbers would you like?"))

    pass_letters = [choice(letters) for _ in range(nr_letters)]
    pass_symbols = [choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_letters + pass_symbols + pass_numbers
    shuffle(password_list)
    generated_password = "".join(password_list)
    pass_input.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    web_text = website_input.get()

    email_text = email_input.get()
    password_text = pass_input.get()

    # Validation
    if len(web_text) == 0 or len(email_text) == 0:
        messagebox.showwarning(title="EMPTY FIELDS",
                               message="Fill all the fields.")
    elif len(password_text) < 8:
        messagebox.showwarning(title="EMPTY FIELDS",
                               message="Password length should be atleast 8")
    else:

        # Confirmation from user
        is_ok = messagebox.askokcancel(
            title="Confirmation", message=f"Details Entered by You \n Website: {web_text} \n Email: {email_text} \n Password: {password_text} \n Is it OK to save?")
        if is_ok:
            with open("./data.txt", "a") as data_file:

                data_file.write(
                    f"{web_text} | {email_text} | {password_text}\n")

                # Reseting the form

                website_input.delete(0, 'end')
                pass_input.delete(0, 'end')
                website_input.focus()


with open("./data.txt", "a") as data_file:
    data_file.write("Website Name/Url | Email | Password\n")

# ---------------------------- UI SETUP ------------------------------- #
screen = tk.Tk()
screen.title("My Pass Manager")
# screen.minsize(width=500, height=500)
screen.config(padx=70, pady=70)


canvas = tk.Canvas(width=200, height=200)
logo_image = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_image)

canvas.grid(row=0, column=1)
# Labels

website_label = tk.Label(text="Website:", font=(54))
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/username:", font=(54))
email_label.grid(row=2, column=0)
pass_label = tk.Label(text="Password:", font=(54))
pass_label.grid(row=3, column=0)

# Entry/ Input fields
website_input = tk.Entry(width=53)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = tk.Entry(width=53, fg='green')
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'viditvarshney222@gmail.com')

pass_input = tk.Entry(width=33)
pass_input.grid(row=3, column=1)


# Buttons
generate_button = tk.Button(
    text="Generate Password", width=15, bd=1, command=generate_pass)
generate_button.grid(row=3, column=2)


add_button = tk.Button(text="Add", width=45, bd=1,
                       bg='light blue', command=save)
add_button.grid(row=4, column=1, columnspan=2)


screen.mainloop()
