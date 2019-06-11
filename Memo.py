"""
import tkinter as tk

window=tk.Tk()
def open():
    pass

def exit():
    window.quit()

menubar = tk.Menu(window)
filemenu=tk.Menu(menubar)

filemenu.add_command(label="열기",command=open)
filemenu.add_command(label="종료",command=exit)    #quit

menubar.add_cascade(label="파일", menu=filemenu)
window.config(menu=menubar)
window.mainloop()
"""

from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

def open():
    file=filedialog.askopenfile(parent=window, mode="r")
    if file !=None:
        lines=file.read()
        text.insert("1.0",lines)
        file.close()

def save():
    file = filedialog.asksaveasfile(parent=window, mode="w")
    if file !=None:
        lines=text.get("1.0",END+"-1c")
        file.write(lines)
        file.close()
def info():
    file = messagebox.showinfo("about, 메모장프로그램")


def exit():
    pass

window = Tk()
text=Text(window, height=30, width=80)
text.pack()

menu=Menu(window)
window.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="저장", command=save)
filemenu.add_command(label="종료", command=exit)
helpmenu=Menu(menu)
menu.add_cascade(label="도움말",menu=helpmenu)
helpmenu.add_command(label="도움말 정보",command=info)

window.mainloop()



