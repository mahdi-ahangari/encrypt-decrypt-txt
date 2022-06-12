from tkinter import *
from tkinter import messagebox

Window = Tk()
Window.geometry("400x400+500+200")
Window.title("password manager")
Window.iconbitmap(bitmap="gray75")

f1 = Frame(Window)        # frame 1 button ha dakheleshe
f1.pack(pady=20)

# -----------------// Master Password //-----------------
def MasterPass():
    secretKey = "Fghcwnv/Rcuuyqtf"    #  encrypted master password
    finalPass = ""
    for i in secretKey :
        finalPass += chr((ord(i)-2))     # takes i asci code decrypt it and turns it to str again
    return finalPass
# -----------------// Master Password //-----------------


# -----------------// command button ha //-----------------

def encrypt():   # Gets all output text and encrypts it
    insideText2 = masterPass.get()                             # gets masterPassword Entry
    if insideText2 == MasterPass():                            #Check if it's True works otherwise shows Error
        insideText = output.get(1.0, "end-1c")
        secretKey = ""
        for i in insideText :
            secretKey += chr(ord(i) + 2)
        clear()
        output.insert(INSERT, secretKey)
        en_button.config(state=DISABLED)        # disabel this button and actives others
        de_button.config(state=NORMAL)
    else:
        messagebox.showerror("password", "wrong password try again !")


def decrypt():      # Gets all output text and decrypts it
    insideText2 = masterPass.get()
    if insideText2 == "Default-Password":
        insideText = output.get(1.0, "end-1c")
        secretKey = ""
        for i in insideText :
            secretKey += chr(ord(i) - 2)
        clear()
        output.insert(INSERT, secretKey)
        de_button.config(state=DISABLED)        # disabel this button and actives others
        en_button.config(state=NORMAL)
    else:
        messagebox.showerror("password", "wrong password try again !")


def clear():      #  clears all the output
    insideText2 = masterPass.get()
    if insideText2 == "Default-Password":
        output.delete(1.0, END)
        en_button.config(state=NORMAL)      # actives both buttons
        de_button.config(state=NORMAL)
    else:
        messagebox.showerror("password", "wrong password try again !")



# -----------------// command button ha //-----------------

# -----------------// button ha //-----------------
en_button = Button(f1, text="encrypt", padx=15, font=("Helvetica", 14), command=encrypt)
de_button = Button(f1, text="decrypt", padx=15, font=("Helvetica", 14), command=decrypt)
clear_button = Button(f1, text="clear", padx=15, font=("Helvetica", 14), command=clear)
# -----------------// button ha //-----------------

# -----------------// Position button ha //-----------------
en_button.grid(row=0, column=1, padx=10)
de_button.grid(row=0, column=2, padx=10)
clear_button.grid(row=0, column=3, padx=10)
# -----------------// Position button ha //-----------------

# -----------------// body //-----------------
Tozihat = Label(Window, text="Encrypt/Decrypt text !!! ", font=("Helvetica", 14))
Tozihat.pack(pady=10)

output = Text(Window, width=45, height=10)
output.pack(pady=10)

Tozihat2 = Label(Window, text="What is Master password ??? ", font=("Helvetica", 14))
Tozihat2.pack()

masterPass = Entry(Window, width=60, show= "*")
masterPass.pack()
# -----------------// body //-----------------

Window.mainloop()