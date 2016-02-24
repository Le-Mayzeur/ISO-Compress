import tkinter,os
from tkinter.filedialog import askopenfile,askdirectory
from tkinter.messagebox import showinfo
import tkinter.ttk

class Convert():
    def __init__(self):        
        self.bg(self.convert,5,20,"Fichier Entrant")
        self.bg(self.convert,5,160,"Fichier Sortant")
        
        self.fonction_entrante()
        self.fonction_sortante()
        
        self.getsame_or_move = tkinter.StringVar()
        b=280
        liste_choix = {1:"Garder dans le meme dossier", 2:"Deplacer dans un autre"}
        for keys,values in liste_choix.items():
            self.choix__=tkinter.Radiobutton(self.convert,text=values, font=("arial",10), variable=self.getsame_or_move, value=keys)
            self.choix__.place(x=8,y=b)
            b+=20
            if keys == 2:
                self.choix__.config(command = self.GoTO_dir)
        self.getsame_or_move.set(1)

        self.format_compatible = ["png","jpeg","ico","jpg","bmp","dib","gif","jfif","jpe","tiff","tif"]
        
        self.bouton1__ = tkinter.Button(self.convert, text = "Ouvrir",relief=tkinter.GROOVE,width=10, font=("courier new",8), command=self.GoTO_dir)
        self.bouton1__.place(x=30, y=325)
        self.bouton2__ = tkinter.ttk.Button(self.convert, text = "Convertir",width=13, command=self.convertir)
        self.bouton2__.place(x=270, y=325)
        
    def From(self):
        self.From = askopenfile(filetypes=[("All","*.ico;*.png;*.jpg;*.bmp,*.dib;*.gif;*.jpeg;*.jfif;*.jpe;*.tiff;*.tif"),
                                        ("fichiers PNG","*.png"),
                                       ("Monochrome Bitmap","*.bmp;*.dib"),
                                       ("fichiers GIF","*.gif"),
                                       ("fichiers JPEG","*.jpg;*.jpeg;*.jfif;*.jpe)"),
                                       ("fichiers TIF","*.tif;*.tiff"),
                                        ("All","*.*"),
                                       ],title="Selectionne le fichier a convertir",initialdir=os.getcwd()[0:3])

    def GoTO_dir(self):
        self.getsame_or_move.set(2)
        self.GoTo = askdirectory(title="Choisis un emplacement",initialdir=os.path.dirname(os.getcwd()))
        
    def fonction_entrante(self):
        self.fichier_source = tkinter.StringVar()
        self.msg__ = tkinter.Checkbutton(self.convert, variable=self.fichier_source, text = "Conserver fichier source", font=("arial",12), bg="white")
        self.msg__.place(x=10, y=45)
        self.fichier_source.set(1)
        
        self.msg__ = tkinter.ttk.Button(self.convert, text = "Rechercher", width=13,command=self.From)
        self.msg__.place(x=270, y=90)

    def fonction_sortante(self):
        self.get_extension = tkinter.StringVar()
        x = 12
        y = 180
        for liste in ["png", "gif", "jpg","","tiff","bmp","ico"]:
            self.aff__=tkinter.Radiobutton(self.convert,text=liste.upper(), variable=self.get_extension, value=liste, bg ="white")
            if y <255:
                self.aff__.place(x=x,y=y)
                y+=25
            else:
                x = 112
                y = 180
        self.get_extension.set("png")

    def convertir(self):
        '''the convert, i can use from PIL import Image istead of cammand'''

        try:
            if self.From.name.split(".")[-1] not in self.format_compatible:
                showinfo("Erreur", "Fichier incompatible", icon='warning')
                self.From = ""
                self.Goto = ""
            else:
                rootname_ = self.From.name
                rootname = rootname_.replace("/","\\")
                nameOnly = os.path.basename(rootname)
                rootChemin = os.path.dirname(rootname)
                Name_without_Ext= ".".join(nameOnly.split(".")[:-1])
                if self.fichier_source.get() == "1" and self.getsame_or_move.get()=="1":
                    os.system("copy {0} {1}\\rescue.{2}".format(rootname,rootChemin,self.get_extension.get()))
                    os.system("rename {0}\\rescue.{1} {2}.{3}".format(rootChemin,self.get_extension.get(),\
                                                                    Name_without_Ext,self.get_extension.get()))
                    self.From = ""
                    self.Goto = ""
                    
                elif self.fichier_source.get() == "0" and self.getsame_or_move.get()== "1":
                    os.system("rename {0} {1}.{2}".format(rootname,Name_without_Ext,self.get_extension.get()))
                    self.From = ""
                    self.Goto = ""
                    
                elif self.fichier_source.get() == "1" and self.getsame_or_move.get()=="2":
                    if self.GoTo != "":
                        os.system("copy {0} {1}\\rescue.{2}".format(rootname,rootChemin,self.get_extension.get()))
                        os.system("rename {0}\\rescue.{1} {2}.{3}".format(rootChemin,self.get_extension.get(),\
                                                                        Name_without_Ext,self.get_extension.get()))
                        os.system("move {0}\\{1}.{2} {3}".format(rootChemin,Name_without_Ext,self.get_extension.get(),self.GoTo))
                        self.From = ""
                        self.Goto = ""
                    else:
                        showinfo("Alerte", "Veuillez fournir une destination\npour le fichier", icon='info')
                    
                elif self.fichier_source.get() == "0" and self.getsame_or_move.get()=="2":
                    if self.GoTo != "":
                        os.system("rename {0} {1}.{2}".format(rootname,Name_without_Ext,self.get_extension.get()))
                        os.system("move {0}\\{1}.{2} {3}".format(rootChemin,Name_without_Ext,self.get_extension.get(), self.GoTo))
                        self.From = ""
                        self.Goto = ""
                    else:
                        showinfo("Alerte", "Veuillez fournir une destination\npour le fichier", icon='info')
                else:
                    self.alerte(150,360)
                
        except AttributeError:
            showinfo("Alerte", "Vous devez selectionner un fichier source", icon='info')
