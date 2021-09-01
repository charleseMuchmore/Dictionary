from tkinter import *
import tkinter as tk
from library import *

def search():
    output_box.delete('1.0', END)
    key = entry_box.get().lower()
    if key in DataBase:
        output_box.insert(END, DataBase.get(key))
    else:
        output_box.insert(END, 'Term not found')

mainWin = Tk()
mainWin.title ("Python Dictionary")
mainWin.configure(background="azure")
mainWin.geometry('270x265')
frame = Frame(mainWin)
frame.pack()

mainMenu = Menu(frame)
# mainMenu.add_command(label = 'Save', command=save)
# mainMenu.add_command(label = 'Edit', command=edit)
# mainMenu.add_command(label = 'View', command=view)

mainLabel = Label(mainWin, text='Python Terminology Dictionary', font=("Times", "10"), bg='azure')
mainLabel.pack()

entry_box = Entry(mainWin)
entry_box.pack()
entry_box.configure(width=20, bg='snow', fg='gray40', font=("Times", "10"))
entry_box.insert (0,"Type Here")


# create_button(mainWin, search, 16)
searchBtn = Button(mainWin, text="Search", font=("Times", "10"), command=search)
searchBtn.configure(width=16)
searchBtn.pack()

output_box = Text(mainWin, width=28, height=10, wrap=WORD, bg='mint cream', font=("Times", "10"))
output_box.pack()


stop = False
while stop == False:
    input1 = input("would you like to edit database? ")
    if input1 == 'no':
        input1 = input("How about now? ")
    elif input1 == 'y' or 'yes':
        inputy = input("would you like to add, delete, or change an item? ")
        if inputy == 'add':
            pass
        elif inputy == 'delete':
            pass
        elif inputy == 'change':
            pass
        else:
            print('false input')
  


mainWin.config(menu = mainMenu)
#mainWin.iconify() #UNHASH THIS CODE WHEN DONE
mainWin.mainloop()



