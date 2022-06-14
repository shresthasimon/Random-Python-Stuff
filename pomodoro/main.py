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
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def resetTime():
    windows.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    titleLabel.config(text="Timer")
    checkMark.config(text="")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global REPS
    REPS+=1

    workSec = WORK_MIN * 60
    shortBreak = SHORT_BREAK_MIN * 60
    longBreak = LONG_BREAK_MIN * 60

    countDown(workSec)
    if REPS % 8 == 0:
        countDown(longBreak)
        titleLabel.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        countDown(shortBreak)
        titleLabel.config(text="Break", fg=PINK)
    else:
        countDown(workSec)
        titleLabel.config(text="Work", fg=GREEN)

    countDown(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    countMin = math.floor(count / 60)
    countSec = count % 60

    if countSec < 10:
        countSec = f"0{countSec}"

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if count > 0:
        global timer
        timer = windows.after(1000, countDown, count - 1)
    else:
        startTimer()
        mark= ""
        workSessions = math.floor(REPS/2)
        for _ in range(workSessions):
            mark += "✔"
        checkMark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Promodoro")
windows.config(padx=100,pady=50, bg=YELLOW)
windows.after(1000, )

titleLabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
titleLabel.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImage)
timerText = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME))
canvas.grid(column=1, row=1)

startButton = Button(text="Start",highlightthickness=0, command=startTimer)
startButton.grid(column=0,row=2)

resetButton = Button(text="Reset", highlightthickness=0, command=resetTime)
resetButton.grid(column=2, row=2)

checkMark = Label(fg=GREEN, bg=YELLOW)
checkMark.grid(column=1, row=3)

windows.mainloop()

