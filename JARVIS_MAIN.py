from tkinter import *
from jarvis import JARVIS
from tkinter.scrolledtext import ScrolledText
#from PIL import Image ,ImageTk
class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)

        #bg_image = PhotoImage(file="jarvis2.jpg")
        #x=Label(image = bg_image)
        #x.grid(row=0,column=0)  

        self.master=master

        self.init_window()
    def init_window(self):
        self.master.title("JARVIS")
        self.pack(fill=BOTH , expand=1)
        self.ask=Entry(self)
        self.ask.place(x=130,y=30)
        self.ask.bind('<Return>',self.geter)
        self.label=ScrolledText (self,width=45,font="MSSerif")
        self.label.place(x=20,y=60)
    def geter(self,event):
        start=1
        self.label.delete(1.0,END)
        self.label.insert(INSERT,JARVIS(self.ask.get()))
        #print(result)

root=Tk()
root.geometry("460x510")
app=Window(root)
root.mainloop()        
        
        
