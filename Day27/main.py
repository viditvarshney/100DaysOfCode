# C to F Scale

from distutils import command
import tkinter as tk


def c_to_f():
    celcius = float(celcius_entry.get())
    far = (celcius * 9/5) + 32
    far_label.config(text=f"{far}")


my_screen = tk.Tk()
my_screen.minsize(width=200, height=200)
my_screen.config(padx=150, pady=100)

# Entry
celcius_entry = tk.Entry(width=12, bd=3, fg="red")
celcius_entry.focus()
celcius_entry.grid(row=1, column=2)


c_label = tk.Label(text="Celcius", font=("Arial", 20, "bold"))
c_label.grid(row=1, column=3)

equal_label = tk.Label(text="is equals to ", font=("Arial", 20, "bold"))
equal_label.grid(row=2, column=2)

far_label = tk.Label(text="0", font=("Arial", 20, "bold"))
far_label.grid(row=2, column=3)


# Button


button = tk.Button(text="Calculate", font=(
    "Arial", 20), bd=5, bg="green", command=c_to_f)
button.grid(row=3, column=3)

my_screen.mainloop()
