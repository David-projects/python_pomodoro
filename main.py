from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔️"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    reps = 0
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps
    reps += 1
    if reps in [2, 4, 7]:
        timer_label.config(text="Break", fg=RED)
        time_countdown(SHORT_BREAK_MIN * 60)
    elif reps in [1, 3, 7 , 7]:
        timer_label.config(text="Work", fg=GREEN)
        time_countdown(WORK_MIN * 60)
    else:
        timer_label.config(text="Break", fg=PINK)
        time_countdown(LONG_BREAK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def time_countdown(count):
    global timer
    minutes = math.floor(count / 60)
    second = count % 60
    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{second}")
    if count > 0:
        timer = window.after(1000, time_countdown, count - 1)
    else:
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK

        check_mark_label.config(text=marks)
        timer_start()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_Image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background_Image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

buttom_start = Button(text="Start", highlightthickness=0, command=timer_start)
buttom_start.grid(column=1, row=3)

buttom_reset = Button(text="Reset", highlightthickness=0, command=timer_reset)
buttom_reset.grid(column=3, row=3)

check_mark_label = Label(text="", bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=2, row=4)

window.mainloop()
