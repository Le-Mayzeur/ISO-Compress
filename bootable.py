import tkinter,os
from tkinter.filedialog import askopenfile,askdirectory
from tkinter.messagebox import showinfo
import tkinter.ttk

class Bootable():
    ''''This part of code is not ready yet'''
    def __init__(self):
        self.bg(self.bootable,5,20,texte="Iso file",height=50)

        self.get_choice = tkinter.StringVar()
        self.liste = tkinter.ttk.Combobox(self.bootable,textvariable = self.get_choice,value=("NTFS","Fat32","FAT"),width=50)
        self.liste.place(x=25,y=154)

        self.get_choice1 = tkinter.StringVar()
        self.liste1 = tkinter.ttk.Combobox(self.bootable,textvariable = self.get_choice1,value=(""),width=50)
        self.liste1.place(x=25,y=204)

        self.get_choice2 = tkinter.StringVar()
        self.liste2 = tkinter.ttk.Combobox(self.bootable,textvariable = self.get_choice2,value=("NTFS","Fat32","FAT"),width=50)
        self.liste2.place(x=25,y=254)

        self.get_choice3 = tkinter.StringVar()
        self.liste3 = tkinter.ttk.Combobox(self.bootable,textvariable = self.get_choice3,value=("NTFS","Fat32","FAT"),width=50)
        self.liste3.place(x=25,y=304)

        
