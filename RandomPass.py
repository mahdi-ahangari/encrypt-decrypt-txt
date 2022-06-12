from tkinter import *
import random
from tkinter.font import ITALIC

def ss():
    window = Tk()
    window.geometry('250x250+600+200')
    window.iconphoto(False, PhotoImage(
        file='D:\programing\python codes\RandomPass\RandomIcon.ico'))
    window.title("RandomPass")
    # window.resizable(False, False)

    # RamzNow = ""


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


    MONITOR = Text(window, bg='silver', width=10, height=0, bd=3, font=("Helvetica", 20), padx=25, pady=30)
    MONITOR.grid(row=0, column=0, columnspan=3, pady=10, padx=25)

    # M_TEXT = Label(window, text="", bg='silver',
    #             font=("", 20, ITALIC), fg='black')
    # M_TEXT.grid(row=0, column=0, sticky=E)

    Guide_T = Label(
        window, text="click button to Create a random password")
    Guide_T.grid(row=1, column=0, pady=10, padx=5, columnspan=3)

    Create = Button(window, text="create", width=13,
                    height=2, bd=5, background="lightgray", command=createrndm)
    Create.grid(row=2, column=0, pady=10, padx=5)
    
    Clear = Button(window, text="clear", width=13,
                    height=2, bd=5, background="lightgray", command=ClearAll)
    Clear.grid(row=2, column=1)


    window.mainloop()

ss()