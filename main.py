import tkinter as tk
from tkinter import ttk
import scrungle as scrung

main_game_window = tk.Tk()

# initializing shit
scr=scrung.score_keeping_system(0, 1, 1, 1, 1)
upgrades=scrung.upgrades()
score_display=tk.Label(master = main_game_window, textvariable = scr.score)
score_display.grid(row=0, column=1)
click_button = tk.Button(master = main_game_window, text="Click me!", command = lambda: scr.click())
click_button.grid(row=0, column=0)

# upgrade button so i don't forget how to make them
upgrade_button_template=tk.Button(master=upgrades.window, command=lambda:scr.click_mod_upgrade(1))

# SHOULD create a button that will open a new window. Does not yet
upgrade_button=tk.Button(master=main_game_window, text="Upgrades", command=lambda:upgrades.window_open())
upgrade_button.grid(row=1, column=0)


main_game_window.mainloop()



