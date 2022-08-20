from tkinter import *
import time
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
    canvas.itemconfig(timer_text, text= "00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", bg= YELLOW, fg= RED, font=(FONT_NAME, 40, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", bg= YELLOW, fg= PINK, font=(FONT_NAME, 40, "bold"))
    else:
        count_down(work_sec)
        timer_label.config(text="Work", bg= YELLOW, fg= GREEN, font=(FONT_NAME, 40, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
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
        marks =""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day 28 - Tkinter, Dynamic Typing, Pomodoro GUI\\tomato.png")
canvas.create_image(100,112, image= tomato_img)
timer_text = canvas.create_text(100,112, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



timer_label = Label(text="Timer", bg= YELLOW, fg= GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1,row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row= 2)

check_mark = Label(bg= YELLOW, fg= GREEN, font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=3)



window.mainloop()