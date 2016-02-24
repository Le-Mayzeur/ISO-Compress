import tkinter
import os
import subprocess
from tkinter.filedialog import askopenfile,askdirectory,askopenfiles
from tkinter.messagebox import showinfo,askyesno,showerror,showwarning
import tkinter.ttk
import time
import threading
import string
import random

class IsoFile():
    def __init__(self,fen):
        ''' the main of part of the iso file converting
        Main de la parti de la conversion de fichier iso'''

        self.bout_loadimg = tkinter.PhotoImage(file="load.png") #Command : call the load_file function...
        self.bout_load = tkinter.ttk.Button(self.iso,image=self.bout_loadimg,command=self.load_file)# ^
        self.bout_load.place(x=300,y=40) 

        self.destin_img = tkinter.PhotoImage(file="dossier.png")
        self.destination = tkinter.ttk.Button(self.iso, image=self.destin_img,command=self.saveas)
        self.destination.place(x=310,y=260)

        self.type = tkinter.ttk.Combobox(self.iso, width=56, values=["UDF-ISO","ISO"],state="readonly")
        self.type.place(x=10,y=160)
        self.type.set("UDF-ISO")

        self.label = tkinter.Label(self.iso,text="")
        self.label.place(x=20,y=280)

        self.label = tkinter.Label(self.iso,text="Nom du label")
        self.label.place(x=25,y=260)
        
        self.get_Name=tkinter.StringVar()
        self.Name_label = tkinter.ttk.Entry(self.iso,width=15,textvariable=self.get_Name)
        self.Name_label.place(x=110,y=260)        

        self.choice_iso = tkinter.StringVar()
        liste2 = {2:"ISO Compression",1:"ISO Boot"}
        a = 220
        for key,texto in liste2.items():
            self.ISOboot_or_ISOcomp = tkinter.ttk.Radiobutton(self.iso, variable = self.choice_iso,text = texto, value=key)
            self.ISOboot_or_ISOcomp.place(x=a,y=50)
            a-= 120
        self.choice_iso.set("2")

        self.start_button = tkinter.Button(self.iso,borderwidth=2,bg="#%02x%02x%02x" % (71,86,82),fg="white", text = "Demarrer", command=lambda:self.conversion(fen))
        self.start_button.place(x=120,y=342)
        
        self.close_button = tkinter.Button(self.iso,borderwidth=2,bg="#%02x%02x%02x" % (71,86,82),fg="white", text = "Annuler", command=fen.destroy)
        self.close_button.place(x=200,y=342)
        
        liste = ["Inclut les fichiers et répertoires cachés.", "Utilise l’heure GMT pour tous les fichiers au lieu de l’heure locale.",""]
        self.choixHidden = tkinter.IntVar()
        self.choixGTL = tkinter.IntVar()
        
        self.check1=self.checkBox(5,185,self.choixHidden,liste[0]) #call the defined checkbox function
        self.check2=self.checkBox(5,205,self.choixGTL,liste[1]) #Appel a la fonction de checkbox definie

        self.choixOptimize = tkinter.IntVar()
        self.check3 = tkinter.Checkbutton(self.iso, text=liste[2],variable=self.choixOptimize,command=self.disable_orNot_3th_checkBox)
        self.check3.place(x=5,y=230) 

        self.image_clean = tkinter.PhotoImage(file="clean.png")
        self.label_clean = tkinter.ttk.Button(self.iso, image=self.image_clean,command=self.cleaning)
        self.label_clean.place(x=210,y=258)
        
        self.Logo()
        self.label_infos()
        
        self.get_optimize = tkinter.StringVar()
        self.Optimize(self.get_optimize) #Call the optimize choice function

        self.savefiles = "" #Pour permettre de creer la valeur, pour eviter l'erreur Attribute
        self.files = "" #Avoid the attribute error, when creating file, if it's empty (empty fields)
        
    def Logo(self):
        self.photo = tkinter.PhotoImage(file="iso2.png")
        self.logo = tkinter.Label(self.iso, image=self.photo)
        self.logo.place(x=10,y=10)

    def cleaning(self):
        '''When pressing the image_clean button:==> Clean the field'''
        self.get_Name.set("")
               
    def label_infos(self):
        '''generer des informations sur le fichier a compresser
        some informations about the file uploaded'''

        self.tab_infos = tkinter.LabelFrame(self.iso,text="Infos sur fichier",height=60,width=360,relief=tkinter.SUNKEN)
        self.tab_infos.place(x=10,y=90)
        self.info = tkinter.Label(self.iso,text="",fg="#%02x%02x%02x" % (96,00,00))
        self.info.place(x=20,y=105)
        self.info2 = tkinter.Label(self.iso,text="",fg="#%02x%02x%02x" % (96,00,00))
        self.info2.place(x=20,y=125)

    def Optimize(self,get_optimize):
        '''Optimize choices function'''

        self.optimize = tkinter.ttk.Combobox(self.iso, width=53, state=tkinter.DISABLED,values=["Optimiser avec l'algorithme de hachage MD5",\
                                                                         "Optimiser avec une comparaison binaire",\
                                                                         "Optimiser en codant les fichiers dupliqués une seule fois",],\
                                                                         textvariable=get_optimize)
        self.optimize.place(x=28,y=230)
        self.optimize.set("Optimiser avec l'algorithme de hachage MD5")
        
    def checkBox(self,x,y,get_choice,texte):
        '''Check box function, some properties'''

        self.choix = tkinter.Checkbutton(self.iso, text=texte,variable=get_choice)
        self.choix.place(x=x,y=y)
        
    def disable_orNot_3th_checkBox(self):
        '''function to disable the third choice within checkbox
        fonction qui est la pour disable ou enable le choix 3 dans les checkbox'''

        if self.choixOptimize.get() == 1:
            self.optimize.config(state=tkinter.NORMAL)
            self.optimize.config(state="readonly")
            
        else:
            self.optimize.config(state=tkinter.DISABLED)

    def lookingfor(self):
        '''On cherche si le fichier a compresser possede les fichiers propres pour une cle bootable
        looking for etfsboot.com file'''

        for dossier in os.listdir(self.files):
            if dossier == "boot":
                boo = self.files+r"boot/etfsboot.com"
                break
            else:
                boo = ""
        return boo
                
    def load_file(self):
        '''Ask the file to compress'''
        self.files=askdirectory(title="Selectionne le dossier",initialdir=os.getcwd()[0:3])
        self.A = self.files
        if self.files != "": #if is empty 
            #Thread for avoiding to wait when the loading finished
            size = threading.Thread(target=self.infos_file)
            size.start()
            
    def infos_file(self):
        '''some design, instead of to print size file with bytes, print it with (kb,mb,Gb)
        how many files, directories, ;-) '''

        self.size_total = 0
        self.nbre_fichier = 0
        self.nbre_dossier = -1
        if os.path.isdir(self.files):
            for dirpath,dirnames,filenames in os.walk(self.files):
                self.nbre_dossier += 1
                for f in filenames:
                    if self.size_total < 16106127360:
                        fp = os.path.join(dirpath,f)
                        self.size_total += os.path.getsize(fp)
                        self.nbre_fichier += 1
                    else:
                        self.size_total = -1
                        break
                if self.size_total == -1:
                    break

        total = self.size_total

        if total > 0:
            fois = 0
            while total > 1024:
                fois += 1
                total /= 1024

            if fois == 0:
                self.size = str(total)+" Bytes"
            else:
                if fois == 1:
                    ext = "Kb"
                elif fois == 2:
                    ext = "Mb"
                else:
                    ext = "Gb"
                size1 = str(total).split(".")
                self.size = size1[0]+"."+size1[1][0]+" "+ext
        else:
            self.size = "Trop volumineux"
            
        try:
            self.out_info.destroy()
            self.out_file_size.destroy()
        except:
            pass
            
        self.info.config(text="Taille du fichier: "+str(self.size))
        self.info2.config(text=str(self.nbre_fichier)+" fichiers au total")

    def configuration(self):
        '''Return the list of configurations, hidden files or not, system file or not ...'''

        if self.choixHidden.get() == 1:
            h = "-h"
        else:
            h = ""
            
        if self.choixGTL.get() == 1:
            g = "-g"
        else:
            g = ""
            
        if self.type.get() == "UDF-ISO":
            typer = "-u1"
        else:
            typer = "-u2"
            
        if self.get_Name.get() != "":
            name = "-l"+self.get_Name.get().upper().replace(" ","")
        else:
            name = ""
            
        if self.choixOptimize.get() == 1:
            if self.get_optimize.get() == "Optimiser avec l'algorithme de hachage MD5":
                opt = "-o"
            elif self.get_optimize.get() == "Optimiser avec une comparaison binaire":
                opt = "-oc"
            else:
                opt = "oi"
        else:
            opt = ""
        config = ["oscdimg.exe","-m"]
        li = [h,name,g,typer,opt]
        for args in li:
            if args != "":
                config.append(args)
                
        return config #Return la liste des configurations 

    def conversion(self,fen):
        '''Convert the directory to Iso '''

        try:
            if self.size != "Trop volumineux": # 
                if self.files != "":
                    if self.savefiles != "":
                        loop = self.lookingfor()
                        annuler = "no"
                        if self.choice_iso.get() == "1":
                            if loop == "": #Decide to create iso, we find etfsboot, we ask if we want to use this file
                                reponse = askyesno("Erreur etfsboot", "Vous avez choisi de faire un iso systeme bootable,qui est indisponible dans le fichier\n\
                                                   Voulez-vous le compresser tout de meme?")
                                if reponse == False:
                                    annuler = "yes"
                                else:
                                    loop = ""
                                                        
                        else: #if not
                            if loop != "":
                                reponse = askyesno("etfsboot trouve", "Vous avez choisi de compresser\n\
                                                   Voulez-vous le compresser en un systeme bootable?")
                                if reponse == False:
                                    loop = ""
                                else:
                                    pass

                        if annuler == "no": #if cancel == no
                            #The progess bar window
                            progress = tkinter.Toplevel()
                            progress.geometry("380x70+{0}+{1}".format(str(fen.winfo_x()),str(int(fen.winfo_y()+220))))
                            progress.title("Conversion...")
                            progress.minsize(380,70)
                            progress.maxsize(380,70)
                            progress.iconbitmap("bmp.ico")
                            progress.grab_set()

                            self.progress = tkinter.ttk.Progressbar(progress,orient="horizontal",length=361, mode="determinate")
                            self.progress.place(x=10,y=35)

                            self.cancel = tkinter.ttk.Button(progress, image=self.image_clean,command=progress.destroy)
                            self.cancel.place(x=340,y=5)

                            cmd = self.configuration()
                            
                            self.label_purcent = tkinter.Label(progress, text="")
                            self.label_purcent.place(x=175,y=10)
                            start = 0
                            niveau = 0
                            if loop != "":
                                cmd.append(loop)
                            cmd.append(self.files)
                            self.name_control = self.code_name()
                            Name = self.get_Name.get()+self.name_control
                            if Name == self.name_control:
                                Name = os.getlogin()+self.name_control
                            full_name = os.path.basename(self.files)+"_"+Name+".iso"
                            #if self.if_iso_already_exist(full_name,os.path.dirname(self.files)):
                                #full_name = os.path.basename(self.files)+"_"+Name+"@.iso"
                            cmd.append(self.savefiles+"/"+full_name)
                            dude = threading.Thread(target = self.ProgressBar, args=(niveau,cmd,Name,progress))
                            dude.start()

                    else:# that's mean the directory is not define, it's empty
                        question = askyesno('Emplacement non defini',"Voulez-vous enregistrer l'ISO au meme endroit ?")
                        if question == False:
                            self.saveas()
                        else: # wants to create the iso file to the same directory
                            self.savefiles = os.path.dirname(self.files)
                            self.conversion(fen)
                
                else: # Didn't choice folder to compress
                    showwarning("ERREUR","Dossier non defini")
            
            else: # Folder is too big , max 15 Gb
                showwarning("ERREUR","Le dossier est trop volumineux")
            
        except AttributeError as Error:
            showerror("ERREUR","Verifiez si c'est bien fait")
        except OSError:#Something wrong is happened   
            showinfo("ERREUR","Quelque chose de mal s'est passe !!!")             
                            
    def if_iso_already_exist(self,iso_name,directory):
        for file in os.listdir(directory):
            if file == iso_name:
                good = True
                break
            else:
                good = False
        return good

    def code_name(self):
        #Avoid some confusions with the name of generated iso file e.g : Iso_chfD54, Iso_Co0fd1
        letters = string.ascii_letters+string.digits
        list_of_code = [random.choice(letters) for _ in range(6)]
        return ''.join(list_of_code)

    def saveas(self): 
        '''get the directory for creating iso file'''
        if self.size != "Trop volumineux":
            self.savefiles=askdirectory(title="Enregistrer le fichier ISO",initialdir=os.getcwd()[0:3])
            self.B = self.savefiles
        else:
            showwarning("ERREUR","Le dossier est trop volumineux")
                
    def algo_tetChaje(self,line,niveau,pourcentage):
        '''Un peu complique, j'ai triche pour regler les pourcentages de progression,
        je ne sais pas comment bien faire simplement'''

        for i in range(1,101):
            if str(i)+"%" in line.rstrip().decode() and i not in pourcentage: #Get all lines from the cmd Dos
                pourcentage.append(i) # get the purcent from the command dos
                niveau = i
                break
        return niveau

    def out_file_info(self,Name,fenetre):
        '''Infos about the new iso file, the new size, the new name if didn't put the name_label'''
        try:
            fenetre.destroy()
            path_ = self.savefiles+"/"+os.path.basename(self.files)+"_"+Name+".iso"
            self.out_info= tkinter.Label(self.iso, text = "Chemin ---> "+path_,fg="blue")
            self.out_info.place(x=20,y=105)
            
            self.out_file_size = tkinter.Label(self.iso,text="Size de l'ISO ---> "+self.calcul_file(os.path.getsize(path_)),fg="blue")
            self.out_file_size.place(x=20,y=125)
            self.backNormal() #Call the back to normal function, clean all widgets
        except OSError as OE:
            showerror("ERREUR",OE) #Error
            
    def backNormal(self):
        '''Back to normal function ! The program can convert another folder'''

        self.info.config(text="")
        self.info2.config(text="")
        self.get_Name.set("")
        self.choixHidden.set(0)
        self.choixGTL.set(0)
        self.optimize.set("Optimiser avec l'algorithme de hachage MD5")
        self.choixOptimize.set(0)
        self.optimize.config(state=tkinter.DISABLED)
        self.type.set("UDF-ISO")
        self.savefiles = ""
        self.files = ""

    def calcul_file(self,iso):
        '''design the size of iso file, (kb,mb,gb)'''

        time = 0
        while iso > 1024:
            time += 1
            iso /= 1024

        if time == 0:
            retour = str(iso)+" Bytes"
        else:
            if time == 1:
                extension = "Kb"
            elif time == 2:
                extension = "Mb"
            else:
                extension = "Gb"
            retour1 = str(iso).split(".")
            retour = retour1[0]+"."+retour1[1][0]+" "+extension

        return retour

    def ProgressBar(self,niveau,cmd,Name,progress):
        '''Progress bar function, some text come from command dos, like the progress purcent'''

        try:
            g = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True,stderr=subprocess.STDOUT, bufsize=1)
            pourcentage = []
            while True:
                self.progress["value"] = niveau
                line = g.stdout.readline(12)
                for i in range(1,101):
                    if str(i)+"%" in line.rstrip().decode() and i not in pourcentage:
                        pourcentage.append(i)
                        niveau = i
                        break
                if not line:
                    break
                self.progress.update()
                self.label_purcent.config(text=str(niveau)+"%", fg="#%02x%02x%02x" % (96,00,00))
        
            self.label_purcent.place(x=150,y=10)
            self.label_purcent.config(text="Complete",fg="blue")
            g.stdout.close()
            g.wait()
        
            affSorti=threading.Thread(target=self.out_file_info,args=(Name,progress))
            affSorti.start()

        except: # Cancel the iso compressing progress
            self.backNormal()
            showwarning("ATTENTION","Annuler une compresion ISO n'est pas bon pour votre ordinateur")
