import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        
        self.label = tk.Label(self.master, text="Enter time (in seconds):")
        self.label.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack()
        
        self.remaining_time = tk.StringVar()
        self.timer_label = tk.Label(self.master, textvariable=self.remaining_time)
        self.timer_label.pack()
        
        self.timer_running = False
        self.start_time = 0
        
    def start_timer(self):
        if not self.timer_running:
            try:
                self.start_time = int(self.entry.get())
                if self.start_time <= 0:
                    raise ValueError
                self.timer_running = True
                self.update_timer()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive integer")
                
    def update_timer(self):
        if self.start_time > 0:
            self.remaining_time.set("Time left: {} seconds".format(self.start_time))
            self.start_time -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.remaining_time.set("Time's up!")
            self.timer_running = False

def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
