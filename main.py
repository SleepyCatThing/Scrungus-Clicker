# Sets everything up to actually run and does it!
# TODO make shit work
# TODO implement saving eventually
# TODO reset button
# TODO dev options???
# TODO actually implement the game button stuff HERE
# TODO implement more stuff appearing through progression via events

import tkinter as tk
from tkinter import ttk
import events as ev


window = tk.Tk()
window.title("Scrungus Clicker")
window.config(width=800, height=600)


# How your 
score = tk.IntVar()
click_mod=1
passive=0

scoreboard=ev.scorer(score, click_mod, passive)

score_display = ttk.Label(master=window, textvariable=score)
score_display.grid(row=0, column=1)

# this probably won't work, need to figure out how to set up tk window in events to hold upgrades!
upgrade_button=tk.Button(master=window, command=ev.buttons)

tk.mainloop()