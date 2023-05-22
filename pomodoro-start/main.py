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
CHECKMARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        countdown(long_break_secs)
        timer_label.config(text="Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        num_work_sessions = reps / 2
        for _ in range(math.floor(num_work_sessions)):
            marks += CHECKMARK
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=2)

# Labels
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=2)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=8, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=8, column=5)

checkmark_label = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=9, column=2)

window.mainloop()
