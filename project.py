from tkinter import *

from graf import showplot
from table import opentabble
from to_json import convertToJSON
from to_json import convertInJSON

root = Tk()
root.title('Графік руху')
root.geometry('400x220')
root.resizable(False, False)
root.configure(bg = 'gray')

def openPlot():
    showplot()

def openTable():
    opentabble()
    root_2 = Tk()
    root_2.geometry('200x100')
    root_2.title('Таблиця')
    lbl = Label(root_2)
    lbl.configure(font = (7), text = "таблиця в консолі")
    lbl.place(x = 0, y = 0)
    root_2.mainloop()

def createJSON():
    convertToJSON()
    root_3 = Tk()
    root_3.geometry('356x70')
    root_3.resizable(False, False)
    root_3.title('файл ')
    lbl = Label(root_3)
    lbl.configure(font = (8), text = 'Файл у форматі JSON сформовано')
    lbl.place(x = 4, y = 2)
    root_3.mainloop()

def create_JSON():
    convertInJSON()
    root_4 = Tk()
    root_4.geometry('356x50')
    root_4.resizable(False, False)
    root_4.title('повідомлення')
    lbl = Label(root_4)
    lbl.configure(font = (10), text = 'Файл у форматі JSON сформовано')
    lbl.place(x = 4, y = 2)
    root_4.mainloop()

btn1 = Button(root)
btn1.configure(bg = 'gray', fg = 'white', text = 'відкрити графік', command = openPlot)
btn1.place(x = -10, y = 0, width = 420, height = 55)

btn2 = Button(root)
btn2.configure(bg = 'gray', fg = 'white', text = 'відкрити таблицю', command = openTable)
btn2.place(x = -10, y = 55, width = 420, height = 55)

btn3 = Button(root)
btn3.configure(bg = 'gray', fg = 'white', text = 'відкрити список основних засобів (JSON)', command = createJSON)
btn3.place(x = -10, y = 110, width = 420, height = 55)
btn4 = Button(root)
btn4.configure(bg = 'gray', fg = 'white', text = 'відкрити  рух (JSON)', command = create_JSON)
btn4.place(x = -10, y = 165, width = 420, height = 55)


root.mainloop()