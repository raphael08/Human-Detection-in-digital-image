from tkinter import Toplevel
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import imutils
protopath = "MobileNetSSD_deploy.prototxt"
modelpath = "MobileNetSSD_deploy.caffemodel"
#caffe = Convolution Architecture for Fast Feature Embedding used for creating image clasfication and alsoimage segementation models
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath) 
#load the model from disk and since we are using caffe model 
#prototxt = this include network layers model contain,each layer parameters ie name,type,input dimension ad output dimensions and also specificaton for connection between layers
#caffemodel =contains weights of the model (weight = are parameters within a NN that transform input data within the netwotk hidden layers)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

idx = 0


def PIL_img2CV_img(PILimg):
    CVimg = cv2.cvtColor(np.asarray(PILimg), cv2.COLOR_RGB2BGR)
    return CVimg


def CV_img2PIL_img(CVimg):
    PILimg = Image.fromarray(cv2.cvtColor(CVimg, cv2.COLOR_BGR2RGB))
    return PILimg




def greyscale(PIL_img):
    if CLASSES[idx]=='person':
        PIL_img = detectedImage(PIL_img)
        CV_img = PIL_img2CV_img(PIL_img)
        CV_gray = cv2.cvtColor(CV_img, cv2.COLOR_BGR2GRAY)
    
        
        return CV_img2PIL_img(CV_gray)





def edge_detect(PIL_img):
    if CLASSES[idx]=='person':
        PIL_img = detectedImage(PIL_img)
        CV_img = PIL_img2CV_img(PIL_img)
        CV_gray = cv2.cvtColor(CV_img, cv2.COLOR_BGR2GRAY)
    
        CV_detected = cv2.Canny(CV_gray, 100, 300)
        return CV_img2PIL_img(cv2.cvtColor(CV_detected, cv2.COLOR_GRAY2BGR))


def detectedImage(PIL_img):
    
    
   
    image = PIL_img2CV_img(PIL_img)
    
    image = imutils.resize(image, width=600)
    
    (H, W) = image.shape[:2]
   
    #dnn - deep neural network
    #blob perform function
      #1. image substraction
      #2. scalling
      #3. And Optionally channel swapping
    blob = cv2.dnn.blobFromImage(image, 1/255, (W, H),(0,0,0),True,crop=False)
    #image = input image want to process before passing it through our deeep neural network for classfiation
    #scalefactor =scale the image by some factor,basically multiplies(scales) the image channels. it scales it down by factor of 1/n 
    #where n is the scalefactor you provide 255 
    #where normally our input model we scalled down the image pixel values between 0-1 instead of 0-255 
    # how much an image size is reduced at each image scale)
    #Size - target size that we want our image to become = (H,W)
    #mean - mean substraction value 
    #swapRB - opencv by default read an image iBGR format but the mean always takes argument in RGB 
    # for b in blob:
    #     for n,img_blog in enumerate(b):
    #         cv2.imshow(str(n),img_blog)

    detector.setInput(blob) #pass blog into the algorithm
    person_detections = detector.forward()  #contain all dectection from model files
    #generate prediction where it return a 4-dimension list
    #the 3rd dimension is our predictions, and each prediction is a list of 7 floating values, At 1 index we have class_id
    #2=confidence/probability 
    # 3-6 coordinate of object detected
    
   
    
    for i in np.arange(0, person_detections.shape[2]): #iterate all over thedetection 
        confidence = person_detections[0, 0, i, 2]   #confidence is found at index 2  
        
       
        if confidence > 0.5:
            global idx
            idx = int(person_detections[0, 0, i, 1]) #confidence is found at index 1

            if CLASSES[idx] != "person":
                continue
            
            person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H]) #coordinates are found at index 3-6, scale the coordinate to our scale image
            (startX, startY, endX, endY) = person_box.astype("int") #calculate the person boundng box

            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2) #draw rectange with (BGR) with red color with 2 thickness
            
  
    
    blue,green,red = cv2.split(image)
    img = cv2.merge((red,green,blue))
    img = Image.fromarray(img)  
    
    return img
    
def blur(PIL_img):
    if CLASSES[idx]=='person':
        PIL_img = detectedImage(PIL_img)
        image = PIL_img2CV_img(PIL_img)
        
        img=cv2.blur(image,(50,50))
        blue,green,red = cv2.split(img)
        img = cv2.merge((red,green,blue))
        img = Image.fromarray(img)  
    

    
        return img
  

