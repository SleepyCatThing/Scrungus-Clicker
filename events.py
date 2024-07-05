# score handling in general
# special events n shit
# obligatory flavor text too
# and all of the buttons and guis! DYnamically! Hopefully!
import tkinter as tk


# TODO add click and passive mult
# TODO more
class scorer:
    def __init__(self, click_mod, passive_mod, click_mult, passive_mult):
        self.score=tk.IntVar()
        self.score.set(0)
        self.click_mod=click_mod
        self.passive_mod=passive_mod
        self.passive_mult=passive_mult
        self.click_mult=click_mult
        
        
    def click_mod_upgrade(self, a):
        self.click_mod+=a
    
    def passive_mod_upgrade(self, a):
        self.passive_mod+=a
    
    def click_mult_upgrade(self, a):
        self.click_mult*=a
        
    def passive_mult_upgrade(self, a):
        self.passive_mod*=a
    
    
    def score_button(self):
        self.score.set(self.score.get()+(self.click_mod*self.click_mult))
    
# TODO buttons functional
# TODO window functional
class buttons:
    def upgrade(self, x, type):
        
        
        
        self.type= {
            "click_mod" : scorer.click_mod_upgrade(x),
            "click_mult" : scorer.click_mult_upgrade(x),
            "passive_mod" : scorer.passive_mod_upgrade(x),
            "passive_mult" : scorer.passive_mult_upgrade(x)
            }
        
        win = tk.Tk()
        
        
        upgrade_button = tk.Button(master=win, command=self.type[type])

        
        win.mainloop()
            