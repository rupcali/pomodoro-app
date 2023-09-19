from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

# RED = "#e7305b"
# PINK = "#D4A1A2"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"

WHITE = "#F6E6E4"
PINK = "#e2979c"
DARK_PINK = "#CA8A8B"
GREEN = "#608474"

FONT_NAME = "Helvetica"
WORK_MIN =25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
    global reps
    reps = 0
     

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
       
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        label_timer.config(text="BREAK", fg=DARK_PINK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label_timer.config(text="BREAK", fg=PINK)
    else:
        count_down(WORK_MIN)
        label_timer.config(text="WORK", fg=GREEN)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in  range(work_sessions):
            marks += "✔️"
        check_mark_label.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=WHITE)

canvas = Canvas(width=204, height=224, bg=WHITE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image= tomato_img)

timer_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=2, row=2)

label_timer = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 30), bg=WHITE)
label_timer.grid(column=2, row=1)

start_button = Button(text="START", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="RESET", command=reset_timer)
reset_button.grid(column=3, row=3)

check_mark_label = Label(bg=WHITE, fg=GREEN ,font=(FONT_NAME, 10, "normal"))
check_mark_label.grid(column=2, row=4)

window.mainloop()
