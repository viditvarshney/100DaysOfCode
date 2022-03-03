import tkinter as tk

ORANGE = '#F3C6C0'
LONG_BREAK = 20
SHORT_BREAK = 5
WORK = 25

repeat = 0
timer = None

# -------------Reset Timer-------------------


def reset_timer():
    screen.after_cancel(timer)
    canvas.itemconfig(count_text, text="00:00")
    timer_label.config(text="Timer")
    check.config(text="")
    global repeat
    repeat = 0


# ------------Countdown logic------------


def countdown(num):
    count_min = num//60
    count_sec = num % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(count_text, text=f"{count_min}:{count_sec}")
    if num > 0:
        global timer

        timer = canvas.after(1000, countdown, num-1)
    else:
        start_countdown()
        check_mark_str = ""
        work_sessions = repeat // 2
        for _ in range(work_sessions):
            check_mark_str += "✔️"
        check.config(text=check_mark_str)


# -----------start timer-------------------


def start_countdown():
    global repeat
    repeat += 1

    work_secs = WORK * 60
    short_secs = SHORT_BREAK * 60
    long_secs = LONG_BREAK * 60

    if repeat % 2 == 0:
        timer_label.config(
            text="Take a Short Break of 5 min.", fg="orange")
        countdown(short_secs)
    elif repeat % 8 == 0:
        timer_label.config(
            text="Time to take a long break of 20 min.", fg="red")
        countdown(long_secs)
    else:
        timer_label.config(text="Work time", fg="green")
        countdown(work_secs)


# ------------------------------------UI ------------------------------------------------------
screen = tk.Tk()
screen.title("A Pomodoro")
# screen.minsize(width=500, height=500)
screen.config(padx=100, pady=150)
screen.config(bg=ORANGE)


# timer label

timer_label = tk.Label(text='TIMER', fg='red', font=(
    'courier', 25, 'bold'), bg=ORANGE)
timer_label.grid(row=0, column=2)

canvas = tk.Canvas(width=268, height=220, bg=ORANGE, highlightthickness=0)
bg_image = tk.PhotoImage(file="./bg_img.png")
canvas.create_image(134, 94, image=bg_image)
count_text = canvas.create_text(134, 190, text="00:00:00", font=(
    "Courier", 30, 'bold'), fill='red')

canvas.grid(row=2, column=2)


# start and reset buttons

reset_button = tk.Button(text="RESET", bg='white', bd=5,
                         width=10, command=reset_timer)
reset_button.grid(row=4, column=1)

start_button = tk.Button(text="START", bg='white', bd=5,
                         width=10, command=start_countdown)
start_button.grid(row=4, column=3)

check = tk.Label(bg=ORANGE, fg="green", font=20)
check.grid(row=5, column=2)


screen.mainloop()
