from tkinter import *
import tkinter as tk
from queue import Empty
from random import setstate
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from turtle import left, width
from PIL import Image,ImageTk
import cv2

from cv2 import blur
import numpy as np
import imutils
import Imageprocessing as pc
import realtimedetection as real
from tkinter import messagebox


class ImageProcessing:
    

    
    image_file = None
    originimage = None
    proceimage = None

    def __init__(self,window):
        # self.window =Tk()
        self.window = window
        self.window.title("IMAGE PROCESSING")
        self.window.geometry("1000x500")
        
        self.frm = Frame(self.window)
        self.frm.pack(padx=15,pady=15,side=BOTTOM)

        self.frame = Frame(self.window)
        self.frame.pack(side=LEFT,pady=10,padx=10,anchor=NW)

        self.frame_right = Frame(self.window)
        self.frame_right.pack(side=LEFT,pady=10,padx=10,anchor=NW)


        self.label = Label(self.frame)
        self.label.pack()



        self.label2 = Label(self.frame_right)
        self.label2.pack()

        self.btn =Button(self.frm,text="browse for image",width=15, command=self.open_image)
        self.btn.pack(side=tk.LEFT)

        self.btn2 = Button(self.frm,text="Exit",width=15,command=window.quit)
        self.btn2.pack(side=tk.LEFT,padx=5)


        self.btn7 =Button(self.frm,text="Real Time Detection",width=15,command=real.main)
        self.btn7.pack(side=tk.LEFT,padx=5)

        self.btn3 =Button(self.frm,bd=0)
        self.btn3.pack(side=tk.LEFT,padx=5)

        self.btn4 =Button(self.frm,bd=0)
        self.btn4.pack(side=tk.LEFT,padx=5)

        self.btn5 =Button(self.frm,bd=0)
        self.btn5.pack(side=tk.LEFT,padx=5)

        self.btn6 =Button(self.frm,bd=0)
        self.btn6.pack(side=tk.LEFT,padx=5)

        # self.window.mainloop()
#edging 
    def edge(self):
        
            self.PIL_detect = pc.edge_detect(self.image_file)
            global proceimage 
            self.proceimage = self.PIL_detect
        
            self.w_box = 450
            self.h_box = 450
            self.showimg(self.image_file, self.label, self.w_box, self.h_box)
            if pc.CLASSES[pc.idx]=='person':
                self.showimg(self.PIL_detect, self.label2, self.w_box, self.h_box)
            else:
             messagebox.showerror('error','no detection found you cant add blur')

    #blur
    def blur(self):
        self.PIL_detect = pc.blur(self.image_file)
        
    
        global proceimage 
        proceimage = self.PIL_detect
    
        self.w_box = 450
        self.h_box = 450
        self.showimg(self.image_file, self.label, self.w_box, self.h_box)
        if pc.CLASSES[pc.idx]=='person':
            self.showimg(self.PIL_detect, self.label2, self.w_box, self.h_box)
        else:
             messagebox.showerror('error','no detection found you cant add blur')
    #resize the image
    def resize(self,w, h, w_box, h_box, pil_image):
        
        self.f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
        self.f2 = 1.0 * h_box / h
        self.factor = min([self.f1, self.f2])
        
        
        self.width = int(self.w * self.factor)
        self.height = int(self.h * self.factor)
    
        return pil_image.resize((self.width, self.height), Image.ANTIALIAS)

    #open and choose image
    def open_image(self):
        
        global image_file
        
        self.filepath = filedialog.askopenfilename()
    
        
        self.image_file = Image.open(self.filepath)

        self.w_box = 450
        self.h_box = 450
       
        self.showimg(self.image_file, self.label, self.w_box, self.h_box)
        self.showimg(self.image_file, self.label2, self.w_box, self.h_box)
        
        self.btn3.config(text="Detect",width=15,command=self.DetectedImage,bd=2)
        

        
    

    #displaying image
    def showimg(self,PIL_img, master, width, height):
        
        
        self.w, self.h = PIL_img.size
        
        
        self.img_resize = self.resize(self.w, self.h, width, height, PIL_img)
        
        self.Tk_img = ImageTk.PhotoImage(image=self.img_resize)
        
        master.config(image=self.Tk_img)
        master.image = self.Tk_img

    #grayscale
    def grayColor(self):
        
                
        self.PIL_detect = pc.greyscale(self.image_file)
        global proceimage 
        self.proceimage = self.PIL_detect
    
        self.w_box = 450
        self.h_box = 450
        self.showimg(self.image_file, self.label, self.w_box, self.h_box)
        if pc.CLASSES[pc.idx]=='person':
            self.showimg(self.PIL_detect, self.label2, self.w_box, self.h_box)
        else:
         messagebox.showerror('error','no detection found you cant add filter')

     #video capture   
    def realTime(self):
        self.w_box = 450
        self.h_box = 450
        image_file = real.main()
        img = PhotoImage(image=image_file)
        self.label.config(image=img)
        self.label.image = img

    #human detection          
    def DetectedImage(self):
        
        self.PIL_detect = pc.detectedImage(self.image_file)
        global proceimage 
        proceimage = self.PIL_detect
    
        self.w_box = 450
        self.h_box = 450
        self.showimg(self.image_file, self.label, self.w_box, self.h_box)
        if pc.CLASSES[pc.idx]=='person':
            self.showimg(self.PIL_detect, self.label2, self.w_box, self.h_box)
            

            self.btn4.config(text="Blur",width=15,command=self.blur,bd=2)
            
            self.btn5.config(text="Grey Scale",width=15,command=self.grayColor,bd=2)
            

            self.btn6.config(text="Edge Detection",width=15,command=self.edge,bd=2)
        else:
          messagebox.showerror('error','no detection found')
       

    

    
if __name__ == '__main__':
    app = ImageProcessing()
    