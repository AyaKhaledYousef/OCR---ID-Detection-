#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 09:52:11 2021
@author: aya
"""
import cv2
import pytesseract 
import matplotlib.pyplot as plt

img = cv2.imread('4.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# =============================================================================
# Detecting words 
# =============================================================================
hImg , wImg , _ = img.shape
boxes = pytesseract.image_to_data(img)   
for x,b in enumerate(boxes.splitlines()):
    print ("x = " ,x)
    if x != 0:
        b=b.split()
        print("b= :",b)
    
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            print("x=",x,"y=",y,"w=",w,"h=",h)
            cv2.rectangle(img,(x,y),(w+x,h+y),(255,0,255),2)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(255,50,0),1)

# =============================================================================
# Face Detection 
# =============================================================================
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
plt.imshow(img)

      
      
      
      
      
      