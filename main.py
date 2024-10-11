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
reps = 0
reset_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(reset_timer)
    label_text.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer, text="00:00")
    label_tick.config(text="")
    start_btn.config(state="normal")  
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def clicked():
    global reps
    reps += 1
    start_btn.config(state="disabled")  
    if reps % 8 == 0:
        label_text.config(fg=RED, text='BREAK')
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label_text.config(fg=PINK, text='BREAK')
        countdown(SHORT_BREAK_MIN * 60)
    else:
        label_text.config(fg=GREEN, text='WORK')
        countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(val):
    count_min = math.floor(val / 60)
    count_sec = val % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')
    if val > 0:
        global reset_timer
        reset_timer = window.after(1000, countdown, val - 1)
    else:
        update_checkmarks()
        
def update_checkmarks():
    msg = ""
    checkmark = "✔"
    for _ in range(math.floor(reps / 2)):
        msg += checkmark
    label_tick.config(text=msg)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(height=400, width=400)
window.title("Pomodoro Timer")
window.config(bg=YELLOW)

canvas = Canvas(window, height=300, width=300, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(150, 150, image=img)
timer = canvas.create_text(150, 170, text='00:00', font=(FONT_NAME, 35, "bold"), fill='white')
canvas.grid(row=2, column=2)

label_text = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label_text.grid(row=1, column=2, pady=(30, 0), padx=(20, 0))

start_btn = Button(window, text='Start', command=clicked)
start_btn.grid(row=3, column=1, padx=(40, 0))

reset_btn = Button(window, text='Reset', command=reset)
reset_btn.grid(row=3, column=3, padx=(0, 40))

label_tick = Label(window, font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
label_tick.grid(row=4, column=2)


start_btn.config(state="normal")

window.mainloop()
