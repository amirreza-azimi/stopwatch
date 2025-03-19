import tkinter as tk
root = tk.Tk()
root.geometry('715x220')
root.resizable(False, False)
root.title('Stopwatch')
running = False
hours, minutes, seconds = 0, 0, 0


def start():
    global running
    if not running:
        update()
        running = True

def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running, hours, minutes, seconds, update_time
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    hours, minutes, seconds = 0, 0, 0
    stopwatch_label.config(text='00:00:00')
    
                           
def update():
    global hours, minutes, seconds, update_time
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    update_time = stopwatch_label.after(1000, update)
text_var = tk.StringVar
stopwatch_label = tk.Label(text='00:00:00', borderwidth=1,width=32, font=('Arial', 80, 'bold'))
stopwatch_label.pack()
start_button = tk.Button(text='start', height=2, width=10, font=('Arial', 20, 'bold'),bd=15, command=start, bg=('light green'))
start_button.pack(side=tk.LEFT)
pause_button = tk.Button(text='pause', height=2, width=10, font=('Arial', 20, 'bold'),bd=15, command=pause, bg=('orange'))
pause_button.pack(side=tk.LEFT)
reset_button = tk.Button(text='reset', height=2, width=10, font=('Arial', 20, 'bold'),bd=15 , command=reset, bg=('powder blue'))
reset_button.pack(side=tk.LEFT)
quit_button = tk.Button(text='quit', height=2, width=10, font=('Arial', 20, 'bold'),bd=15, command=root.quit, bg=('red'))
quit_button.pack(side=tk.LEFT)
root.mainloop()
