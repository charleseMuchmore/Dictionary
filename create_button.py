from tkinter import *

def create_button(windo, command, widt):
    
    searchBtn = Button(windo, text="Search", font=("Times", "10"), command=command)
    searchBtn.configure(width=widt)
    searchBtn.pack()