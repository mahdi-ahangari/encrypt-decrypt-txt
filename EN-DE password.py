from tkinter import *
from tkinter import messagebox

Window = Tk()
Window.geometry("400x400+500+200")
Window.title("password manager")
Window.resizable(False, False)
Window.iconbitmap(bitmap="gray75")

f1 = Frame(Window)        # frame 1 button ha dakheleshe
f1.pack(pady=20)

# -----------------// Master Password //-----------------
secretKey = "Fghcwnv/Rcuuyqtf"

        # -------------// ave TxT Password //-----------------
def writeSecret():
    global secretKey
    with open("secretkey.TXT", "r+") as f:
        X = f.readlines()[0:]
        if "Fghcwnv/Rcuuyqtf" not in X and len(X)<2:
            f.truncate()
            f.write("Please Don't Change anything, if you want to reset password just delete file\n")
            f.write("Fghcwnv/Rcuuyqtf")
        try:
            secretKey = X[1].rstrip()
        except IndexError:
            pass
writeSecret()
        # -------------// Save TxT Password //-----------------

def MasterPass(Key):
    finalPass = ""
    for i in Key :
        finalPass += chr((ord(i)-2))     # takes i asci code decrypt it and turns it to str again
    return finalPass
# -----------------// Master Password //-----------------


# -----------------// command button ha //-----------------


def encrypt():   # Gets all output text and encrypts it
    insideText2 = masterPass.get()                             # gets masterPassword Entry
    if insideText2 == MasterPass(secretKey):                            #Check if it's True works otherwise shows Error
        insideText = output.get(1.0, "end-1c")
        Result = ""
        for i in insideText :
            Result += chr(ord(i) + 2)
        clear()
        output.insert(INSERT, Result)
        en_button.config(state=DISABLED)        # disabel this button and actives others
        de_button.config(state=NORMAL)
    else:
        messagebox.showerror("password", "wrong password try again !")


def decrypt():      # Gets all output text and decrypts it
    insideText2 = masterPass.get()
    if insideText2 == MasterPass(secretKey):
        insideText = output.get(1.0, "end-1c")
        Result = ""
        for i in insideText :
            Result += chr(ord(i) - 2)
        clear()
        output.insert(INSERT, Result)
        de_button.config(state=DISABLED)        # disabel this button and actives others
        en_button.config(state=NORMAL)
    else:
        messagebox.showerror("password", "wrong password try again !")


def clear():      #  clears all the output
    insideText2 = masterPass.get()
    if insideText2 == MasterPass(secretKey):
        output.delete(1.0, END)
        en_button.config(state=NORMAL)      # actives both buttons
        de_button.config(state=NORMAL)
    else:
        messagebox.showerror("password", "wrong password try again !")



# -----------------// command button ha //-----------------

# -----------------// button ha //-----------------
en_button = Button(f1, text="encrypt", padx=15, font=("Helvetica", 14),bd=2, bg='lightgray', command=encrypt)
de_button = Button(f1, text="decrypt", padx=15, font=("Helvetica", 14),bd=2, bg='lightgray', command=decrypt)
clear_button = Button(f1, text="clear", padx=15, font=("Helvetica", 14),bd=2, bg='lightgray', command=clear)
# -----------------// button ha //-----------------

# -----------------// Position button ha //-----------------
en_button.grid(row=0, column=1, padx=10)
de_button.grid(row=0, column=2, padx=10)
clear_button.grid(row=0, column=3, padx=10)
# -----------------// Position button ha //-----------------

# -----------------// body //-----------------
Tozihat = Label(Window, text="Encrypt/Decrypt text !!! ", font=("Helvetica", 14))
Tozihat.pack(pady=10)

output = Text(Window, width=45, height=10, bd=3, bg='silver')
output.pack(pady=10)

Tozihat2 = Label(Window, text="What is Master password ??? ", font=("Helvetica", 14))
Tozihat2.pack()

masterPass = Entry(Window, width=60, show= "*", bd=3, bg='silver')
masterPass.pack()
# -----------------// body //-----------------

f2 = Frame(Window)        # frame 2 button ha dakheleshe
f2.pack(pady=5, padx=19, fill="x")

# -----------------// Change Password section (inside window2) //-----------------
W2exist = False


def NewWindow():
    global W2exist
    if not W2exist:
        Window2 = Toplevel()
        Window2.focus_force()
        Window2.geometry("400x130+550+350")
        Window2.title("Change Password")
        Window2.resizable(False, False)
        W2exist = True
        l1 = Label(Window2, text="you can change master password only if you know the\n\
        original wich means only if i want you to know :)", font=("Helvetica", 13)).grid(row=0, column=0, columnspan=2)

        l2 = Label(Window2, text="enter original password :").grid(row=1, column=0, sticky=W)
        masterPass = Entry(Window2, width=30, show= "*", bd=3, bg='silver')
        masterPass.grid(row=1, column=0, sticky=E)

        l2 = Label(Window2, text="enter new password :").grid(row=2, column=0, sticky=W)
        newPass = Entry(Window2, width=30, bd=3, bg='silver')
        newPass.grid(row=2, column=0, sticky=E)

        l3 = Label(Window2,width=50).grid(row=4, column=0, sticky=W) # hidden Lable for fixing grid system

        # -------------// Confirm Change Password Button (inside window2) //-------------
        
        
        def Change():
            global secretKey                   # daryaft har 2 input , check sehat original pass , change new one to original
            oldPassword = masterPass.get()
            newPassword = newPass.get()
            if oldPassword == MasterPass(secretKey):
                En_newPass = ""
                for i in newPassword:
                    En_newPass += chr((ord(i)+2))
                
                with open("secretkey.TXT", "r+") as f:
                    f.truncate()
                    f.write("Please Don't Change anything\n")
                    f.write(En_newPass)
            else:
                messagebox.showerror("password", "wrong password try again !")
                Window2.focus_force()
        
        ChangePass = Button(Window2, text="Change Masster Password", bg='lightgray', font=("Helvetica", 10), command=Change)
        ChangePass.grid(row=3, column=0, pady=10)

        Exit2 = Button(Window2, text="EXIT", bg='gray', padx=8, relief="groove", bd=4, font=("Helvetica", 7), command=Window.destroy)
        Exit2.grid(row=3, column=0, pady=15,sticky=E)
        
        
        # -------------// Confirm Change Password Button (inside window2) //-------------



ChangePass = Button(f2, text="Change Masster Password", bg='lightgray', font=("Helvetica", 10), command=NewWindow)
ChangePass.pack(side=LEFT)
# -----------------// ↑ enter to Change Password section Button ↑ //-----------------


# -----------------// Exit Button //-----------------
Exit = Button(f2, text="EXIT", bg='gray', relief="groove", bd= 5, font=("Helvetica", 10), command=Window.destroy)
Exit.pack(side=RIGHT)
# -----------------// Exit Button //-----------------

Window.mainloop()