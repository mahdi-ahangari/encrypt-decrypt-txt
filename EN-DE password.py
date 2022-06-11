from tkinter import *
from turtle import width

Window = Tk()
Window.geometry("400x400+500+200")
Window.title("password manager")
Window.iconbitmap(bitmap="gray75")

f1 = Frame(Window)        # frame 1 button ha dakheleshe
f1.pack(pady=20,)
# -----------------// command button ha //-----------------
def encrypt():
    pass
def decrypt():
    pass
def clear():
    pass
# -----------------// command button ha //-----------------

# -----------------// button ha //-----------------
en_button = Button(f1, text="encrypt", padx=20, font=("Helvetica", 14), command=encrypt)
de_button = Button(f1, text="decrypt", padx=20, font=("Helvetica", 14), command=decrypt)
clear_button = Button(f1, text="clear", padx=20, font=("Helvetica", 14), command=clear)
# -----------------// button ha //-----------------

# -----------------// Position button ha //-----------------
en_button.grid(row=0, column=1, padx=10)
de_button.grid(row=0, column=2, padx=10)
clear_button.grid(row=0, column=3, padx=10)
# -----------------// Position button ha //-----------------

# -----------------// body //-----------------
Tozihat = Label(Window, text="Encrypted/Decrypted text !!! ", font=("Helvetica", 14))
Tozihat.pack(pady=10)

output = Text(Window, width=45, height=10)
output.pack(pady=10)

Tozihat2 = Label(Window, text="Enter your password", font=("Helvetica", 14))
Tozihat2.pack()

entery = Entry(Window, width=60, show= "*")
entery.pack()
# -----------------// body //-----------------

Window.mainloop()