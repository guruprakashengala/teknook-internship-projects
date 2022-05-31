#importing required packages
import tkinter as tk
# declaring variables
running = False
hours,minutes,seconds = 0,0,0

# defining functions
def resume():
    global running
    if not running:
        update()
        running = True
def start():
    global running
    if not running:
        update()
        running = True
def pause():
    global running
    if running:
        stopwatch_lable.after_cancel(update_time)
        running = False
def reset():
    global running
    if running:
        stopwatch_lable.after_cancel(update_time)
        running =False
    global hours,minutes,seconds
    hours,minutes,seconds = 0,0,0
    stopwatch_lable.config(text='00:00:00')
def update():
    global hours,minutes,seconds
    seconds  += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    hours_string = f'{hours}'if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}'if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}'if seconds > 9 else f'0{seconds}'
    stopwatch_lable.config(text=hours_string+':'+minutes_string+':'+seconds_string)
    global update_time
    update_time = stopwatch_lable.after(1000,update)

#creating tkinter window object
root = tk.Tk()
root.geometry('485x220')
root.title('Stop Watch')

#creating display screen for timer
stopwatch_lable = tk.Label(text='00:00:00',font=('Arial',80))
stopwatch_lable.pack()

# creating buttons
start_button = tk.Button(text='Start',height=5,width=6,font=('Arial',20),command=start)
start_button.pack(side=tk.LEFT)
start_button = tk.Button(text='Pause',height=5,width=6,font=('Arial',20),command=pause)
start_button.pack(side=tk.LEFT)
start_button = tk.Button(text='resume',height=5,width=6,font=('Arial',20),command=resume)
start_button.pack(side=tk.LEFT)
start_button = tk.Button(text='Reset',height=5,width=6,font=('Arial',20),command=reset)
start_button.pack(side=tk.LEFT)
start_button = tk.Button(text='Exit',height=5,width=6,font=('Arial',20),command=root.quit)
start_button.pack(side=tk.LEFT)

#running the Tkinter App
root.mainloop()