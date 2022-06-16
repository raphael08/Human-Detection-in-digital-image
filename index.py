from re import I
from tkinter import *
from tkinter.ttk import Progressbar
import sys
from turtle import width
import cv2
import imutils
from PIL import Image,ImageTk
import application as ap



root = Tk()
root.resizable(0,0)
height = 430
width = 530

x = (root.winfo_screenwidth()//2)-(width//2)

y = (root.winfo_screenheight()//2)-(height//2)


 
root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
root.wm_attributes('-topmost',True)
# root.wm_attributes('-alpha',0.9)

root.overrideredirect(1)    


root.config(background="#6699FF")


exitButton = Button(root,text='X',command=root.destroy,font=('arial',10,'bold'),fg='yellow',
bg="#6699FF",bd=0,activebackground="#6699FF")
exitButton.place(x=500,y=10)

welcome_label = Label(root,text="Welcome G2 App".upper(),font=('yu gothic ui',20,'bold'),bg="#6699FF")
welcome_label.place(x=150,y=15)
subject_label = Label(root,text="DIGITAL IMAGE PROCESSING".upper(),font=('yu gothic ui',8,'italic'),bg="#6699FF")
subject_label.place(x=190,y=60)
img =(Image.open("ditlogo.png"))
resize = img.resize((250,250),Image.ANTIALIAS)


image = ImageTk.PhotoImage(resize)
logo_label = Label(root,image=image,bg="#6699FF")
logo_label.place(x=150,y=90)


progress_label = Label(root,text='Please Wait Loading......',font=('yu gothic ui',8,'bold'),bg="#6699FF")
progress_label.place(x=190,y=350)

progress = Progressbar(root,orient=HORIZONTAL,length=500,mode='determinate')
progress.place(x=15,y=390)

def exit():
       sys.exit(root.destroy())

       
def top():
    
    
    win = Toplevel()
    ap.ImageProcessing(win)
    root.withdraw()
    win.grab_set()
     #loading page withdraw from background
    win.deiconify()

     #app page pop up


i=0


def load():
 global i
 if i <=10:
        txt = 'Please wait Loading .....'+(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(500,load)
        progress['value'] = 10*i
        i += 1
 else:
       #  win = Toplevel()
       #  ap.ImageProcessing(win)
       #  root.withdraw() #loading page withdraw from background
       #  win.deiconify()

        top()
        
      
       

load()


root.mainloop()