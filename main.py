# Sets everything up to actually run and does it!


import tkinter as tk
from tkinter import ttk
import events as ev


window = tk.Tk()
window.title("Scrungus Clicker")
window.config(width=800, height=600)

score = tk.IntVar()
click_mod=1
passive=0

scoreboard=ev.scorer(score, click_mod, passive)

score_display = ttk.Label(master=window, textvariable=score)
score_display.grid(row=0, column=1)




tk.mainloop()