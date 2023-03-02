import time
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔ "
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    pomodoro_label.config(text="Timer", fg=RED)
    check_mark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        pomodoro_label.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        pomodoro_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
        count_down(short_break_sec)
    else:
        pomodoro_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += CHECK_MARK
        check_mark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# def say_somentinhg(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# window.after(1000, say_somentinhg, 1, 2, 3)

pomodoro_label = Label()
pomodoro_label.config(text="Timer", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
pomodoro_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW)
start_button.grid(row=2, column=0)
start_button.config(command=start_timer)

check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)
reset_button.config(command=reset_timer)



window.mainloop()
