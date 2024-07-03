# score handling in general
# special events n shit
# obligatory flavor text too
# and all of the buttons and guis! DYnamically! Hopefully!
import tkinter as tk


# TODO add click and passive mult
# TODO more
class scorer:
    def __init__(self, click_mod, passive):
        self.score=tk.IntVar()
        self.score.set(0)
        self.click_mod=click_mod
        self.passive=passive
    
    def click_mod_upgrade(self, a):
        self.click_mod+=a
    
    def passive_upgrade(self, a):
        self.passive+=a
    
    def score_button(self):
        self.score.set(self.score.get()+self.click_mod)
    
# TODO buttons functional
# TODO window functional
class buttons:
    def upgrade_window(self):
        win = tk.Tk()
        # pseudo code because I ran out of time. Hopefully I will understand what I meant later!
        click upgrades button = tk.button(master=win, command=popuptypething)
        click_upgrades=popup_type_thing(master=win)
        click_upgrade_1=tk.Button(master=click_upgrade_window, command=scorer.click_mod_upgrade(1))
        click_upgrade_1.grid(row=0, column=0)
        
        win.mainloop()
            
    
    
    def upgrade(self, b, type):
        if (type=="cm"):
            scorer.click_mod_upgrade(b)
        elif (type=="passive"):
            scorer.passive_upgrade(b)