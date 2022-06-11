from tkinter import *

Window = Tk()
Window.geometry("400x450+500+200")
Window.title("password manager")
Window.iconbitmap(bitmap="gray75")

f1 = Frame(Window)
f1.pack(pady=20)

def encrypt():
    pass
def decrypt():
    pass
def clear():
    pass

en_button = Button(f1, text=" ",padx=50, command=encrypt)
de_button = Button(f1, text=" ",padx=50, command=decrypt)
clear_button = Button(f1, text=" ",padx=50, command=clear)

en_button.grid(row=0, column=1)
de_button.grid(row=0, column=2)
clear_button.grid(row=0, column=3)

Window.mainloop()