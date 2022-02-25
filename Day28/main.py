from ast import Or
import tkinter as tk

ORANGE = '#F3C6C0'

# ------------------------------------UI ------------------------------------------------------

screen = tk.Tk()
screen.title("A Pomodoro")
# screen.minsize(width=500, height=500)
screen.config(padx=100, pady=150)
screen.config(bg=ORANGE)
# timer label

timer_label = tk.Label(text='TIMER', fg='red', font=('courier', 25, 'bold'))
timer_label.grid(row=0, column=2)

canvas = tk.Canvas(width=268, height=220, bg=ORANGE, highlightthickness=0)
bg_image = tk.PhotoImage(file="./bg_img.png")
canvas.create_image(134, 94, image=bg_image)
canvas.create_text(134, 190, text="00:00:00", font=(
    "Courier", 30, 'bold'), fill='red')

canvas.grid(row=2, column=2)


# start and reset buttons

reset_button = tk.Button(text="RESET", bg='white', bd=5, width=10)
reset_button.grid(row=4, column=1)

start_button = tk.Button(text="START", bg='white', bd=5, width=10)
start_button.grid(row=4, column=3)

check = tk.Label(text="✔️", bg=ORANGE, fg="green", font=20)
check.grid(row=5, column=2)

screen.mainloop()
