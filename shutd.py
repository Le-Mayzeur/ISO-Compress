import tkinter
import os
import time
from subprocess import Popen,PIPE,STDOUT

class Shutd():
    def __init__(self,fen):
        self.bg(self.shutdown,5,160,"Dans combien de temps ?")
        self.bg(self.shutdown,5,20,"Eteindre ou Redemarrer ?")
        
        self.choice_get = tkinter.StringVar()
        liste = {"Shutdown":40,"Restart":230}
        for txt,key in liste.items():
            self.radio = tkinter.Radiobutton(self.shutdown,bg='white', text = txt, font=("arial",13),variable = self.choice_get, value=txt, anchor="w",pady=15)
            self.radio.place(x=key,y=50)
        
        self.message_alert = tkinter.Label(self.shutdown,text="", fg="red", font=("arial",14))
        self.message_alert.place(x=130,y=290)

        self.hour = tkinter.IntVar()
        self.time("Heure",20,210,60,210,self.hour)

        self.minute = tkinter.IntVar()
        self.time("Minute",134,210,180,210,self.minute)

        self.second = tkinter.IntVar()
        self.time("Seconde",255,210,308,210,self.second)
        
        self.bouton = tkinter.Button(self.shutdown, text = "Valider", relief=tkinter.GROOVE,command=lambda:self.validate(fen), width = 20)
        self.bouton.place(x=170,y=330)

        self.image()
        
    def time(self,label,a,b,x,y,time_get):
        '''timer board'''

        self.label_time = tkinter.Label(self.shutdown, text = label, fg="#%02x%02x%02x" % (71,86,82))
        self.label_time.place(x=a,y=b)
        self.spin = tkinter.Spinbox(self.shutdown, from_=0, to=60, textvariable = time_get, font=("arial",10),width=5)
        self.spin.place(x=x,y=y)

    def get_all_second(self):
        try:
            self.all_second = self.second.get()+((self.minute.get()+(self.hour.get()*60))*60)
        except ValueError:
            self.all_second=0
        return self.all_second

    def text_screen(self):
        if self.hour.get() == 0:
            if self.minute.get() == 0:
                self.text=self.choice_get.get()+" dans moins de: "+str(self.second.get())+" seconde(s)"
            elif self.minute.get() != 0 and self.second.get() == 0:
                self.text=self.choice_get.get()+" dans moins de: "+str(self.minute.get())+" minute(s)"
            elif self.minute.get() != 0 and self.second.get() != 0:
                self.text=self.choice_get.get()+" dans moins de: "+str(self.minute.get())+" minute(s) et "+str(self.second.get())+" seconde(s)"
        else:
            if self.minute.get() == 0:
                if self.second.get() ==0:
                    self.text=self.choice_get.get()+" dans moins de: "+str(self.hour.get())+" heure(s)"
                else:
                    self.text=self.choice_get.get()+" dans moins de: "+str(self.hour.get())+" heure(s) et "+str(self.second.get())+" seconde(s)"
            else:
                if self.text_second.get() ==0:
                    self.text=self.choice_get.get()+" dans moins de: "+str(self.hour.get())+" heure(s) et "+str(self.minute.get())+" minute(s)"
                else:
                    self.text=self.choice_get.get()+" dans moins de: "+str(self.hour.get())+" heure(s) et "+str(self.minute.get())+" minute(s) et "+str(self.second.get())+" seconde(s)"       
    
        return self.text

    def validate(self,fen):
        try:
            if (self.hour.get() == 0 and self.minute.get() ==0 and self.second.get() == 0):
                self.message_alert.config(text="Vous devez preciser l'heure")
            elif not self.choice_get.get():
                 self.message_alert.config(text="Restart or Shtdown ??")
            else:
                self.message_alert.destroy()
                self.bouton.destroy()
                cmd = ["Shutdown", '/'+self.choice_get.get()[0],'/f','/c',"'"+self.text_screen()+"'","/t",str(self.get_all_second())]
                h = Popen(cmd,stdout=PIPE, shell=True,stderr=STDOUT)
                with open("history", "a") as history:
                    history.write(time.strftime("%A %d %B %Y %H:%M:%S")+"\n"+str(self.get_all_second())+"\n"+self.choice_get.get()+"\n\n")
        except ValueError:
            self.message_alert.config(text="Format Heure Invalide")
                
    def image(self):
        self.photo = tkinter.PhotoImage(file="logo_shut.png")
        self.image = tkinter.Label(self.shutdown, image=self.photo)
        self.image.place(x=10,y=285)
