import tkinter
import math
from tkinter.ttk import Notebook
from convert import *
from shutd import *
from isoFile import *
from bootable import *
'''This program is not perfect -- > Ce programme n'est pas parfait '''
# Je vous met le code source, essayer de l'ameliorer, cela m'aidera et vous aussi, merci
# here is my code source, try to optimize it, this'll help me and you too, thank you.
#---------Le-Mayzeur -- rynnika@gmail.com ------------ #

class Setup(tkinter.Frame,Shutd,Convert,IsoFile,Bootable):
    def __init__(self,fen):
        tkinter.Frame.__init__(self,bg = "#%02x%02x%02x" % (71,86,82))
        self.grid()
        
        #Header
        self.title = tkinter.Label(self, text="Le-Mayzeur", fg="white", font=("bauhaus 93",22), bg = "#%02x%02x%02x" % (71,86,82))
        self.title.grid(row=0, column = 0)
        
        #Body
        onglet=Notebook(self, width=380, height=380)

        self.convert=tkinter.ttk.Panedwindow(orient=tkinter.VERTICAL)
        self.iso=tkinter.ttk.Panedwindow(orient=tkinter.VERTICAL)
        self.shutdown=tkinter.ttk.Panedwindow(orient=tkinter.VERTICAL)
        self.bootable=tkinter.ttk.Panedwindow(orient=tkinter.VERTICAL)

        onglet.add(self.iso,text='ISO file')
        onglet.add(self.convert,text='Convert')
        onglet.add(self.shutdown, text="Shutdown")
        onglet.add(self.bootable,text='Boot drive')
        onglet.grid(row=2, column=0)

        #Links --. inherit classes
        Convert.__init__(self)
        Shutd.__init__(self,fen)
        IsoFile.__init__(self,fen)
        Bootable.__init__(self)
        
        #footer
        self.footer = tkinter.Label(fen, width=480, bg="#%02x%02x%02x" % (71,86,82))
        self.footer.place(x=0,y=447)
        self.footer = tkinter.Label(fen, text="rynnika@gmail.com", fg="white", bg="#%02x%02x%02x" % (71,86,82))
        self.footer.place(x=130,y=447)

        #Title frames
    def bg(self,v,x,y,texte,color="white",height=104):
        self.canvas__ = tkinter.Canvas(v, bg="#%02x%02x%02x" % (71,86,82), width=365, height=height+6)
        self.canvas__.place(x=x,y=y)
        self.canvas__ = tkinter.Canvas(v, bg=color, width=359, height=height)
        self.canvas__.place(x=x+3,y=y+3)
        self.title = tkinter.Label(v, text = texte,font=("arial",10),bg="white")
        self.title.place(x=x+25, y=y-6)
        
if __name__ == "__main__":
    fen  = tkinter.Tk()
    Setup(fen)
    fen.title("Le-Mayzeur")
    fen.geometry("380x470+"+str(int(fen.winfo_screenwidth()/3))+"+10")
    fen.iconbitmap("bmp.ico")
    fen.minsize(380,470)
    fen.maxsize(380,470)
    fen.mainloop()
