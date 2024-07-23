import tkinter as tk
import time

# This class handles keeping your score, and keeping track of how you gain that score, and updating that score!
class score_keeping_system:
    def __init__(self, score, click_mod, click_mult, passive_mod, passive_mult):
        self.score=tk.IntVar()
        self.score.set(score)
        self.click_mod=click_mod
        self.click_mult=click_mult
        self.passive_mod=passive_mod
        self.passive_mult=passive_mult
        
    def click(self):
        sc=self.score.get()
        self.score.set(sc+(self.click_mod*self.click_mult))
        
    def click_mod_upgrade(self, value):
        self.click_mod+=value
        
    def click_mult_upgrade(self, value):
        self.click_mult*=value
        
    def passive_mod_upgrade(self, value):
        self.passive_mod+=value
    
    def passive_mult_upgrade(self, value):
        self.passive_mult*=value
        
# This class is intended to cut some of the clutter from main by setting up the grid itself, and EVENTUALLY will show the tooltips!
class upgrades():
    def __init__(self):
        self.window=tk.Toplevel()
        self.x=0
        self.y=0

    
    def upgrade(self, button):
        button.grid(row=self.x, column=self.y)
        if (self.x<5):
            self.x+=1
        else:
            self.x=0
            self.y+=1
    
    def window_open(self):
        self.window.mainloop()