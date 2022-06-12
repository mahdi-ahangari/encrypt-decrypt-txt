from tkinter import *
import random
from tkinter.font import ITALIC
from tkinter import messagebox
import clipboard

def Runapp():
    window = Tk()
    window.geometry('250x250+600+200')
    window.iconphoto(False, PhotoImage(
        file='D:\programing\python codes\RandomPass\RandomIcon.ico'))
    window.title("RandomPass")
    window.resizable(False, False)

    # RamzNow = ""

# -----------------// command button ha //-----------------
    def createrndm():
        #65 - 122
        Ramz = ""
        for i in range(8):
            # random aski coede into chr 8 times
            B = random.randint(65, 122)
            Ramz += chr(B)
        MONITOR.delete(1.0, END)
        MONITOR.insert(INSERT, Ramz)


    def ClearAll():
        MONITOR.delete(1.0, END)      
    

    def copykon():
        clipboard.copy(MONITOR.get(1.0, "end-1c"))
        messagebox.showinfo("Copy", "Password Copied to clip board seccesfully") 
        ClearAll()


# -----------------// command button ha //-----------------

    MONITOR = Text(window, bg='silver', width=10, height=0, bd=3, font=("Helvetica", 20), padx=25, pady=30)
    MONITOR.grid(row=0, column=0, columnspan=3, pady=10, padx=25)


    Guide_T = Label(
        window, text="click button to Create a random password")
    Guide_T.grid(row=1, column=0, pady=5, padx=5, columnspan=3)

# -----------------// button ha //-----------------
    Create = Button(window, text="create", width=13,
                    height=2, bd=4, background="lightgray", command=createrndm)
    Create.grid(row=2, column=0, pady=5, padx=5)
    
    Clear = Button(window, text="clear", width=13,
                    height=2, bd=4, background="lightgray", command=ClearAll)
    Clear.grid(row=2, column=1)

    Copyto = Button(window, text="Copy to Clipboard", width=14,  #  gets what is inside and copy it to clipboard
                    height=2, bd=3, background="lightgray", command= copykon)
    Copyto.grid(row=3, column=0)

    Exit = Button(window, text="EXIT", padx=10, bg='gray', relief="groove", bd= 5, font=("Helvetica", 10), command=window.destroy)
    Exit.grid(row=3, column=1, pady=5, padx=5)
# -----------------// button ha //-----------------

    window.mainloop()