#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:47:58 2019

@author: Jo
"""
#Doing with open cv2
#Import Cv2 library
import numpy as np
import cv2,os
from moviepy.editor import VideoFileClip

#location of the input files
inputfilepaths=["Dataset/big1.mp4","Dataset/big2.mp4","Dataset/big3.mp4","Dataset/big4.mp4"
                ,"Dataset/big5.mp4","Dataset/big6.mp4","Dataset/big7.mp4"]

#For saving output   
if not os.path.exists('Frames'):
    os.makedirs('Frames')

video=[]
#location of video file
for x in range(0,len(inputfilepaths)):
    video.append(cv2.VideoCapture(inputfilepaths[x]))
    print(x+1,"Video length ",VideoFileClip(inputfilepaths[0]).duration,"seconds")

def extractframe(sec):
    # cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000) is responsible for 
    #skipping directly to the sec in the video (sec*1000th millisecond)
    
        #reading frame
    hasframes=np.array([])
 
    for x in range(0,len(video)):
        video[x].set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
        hasimage,images=video[x].read()
        hasframes=np.append(hasframes,hasimage)
       
    if hasframes[len(hasframes)-1]:
        #Write to location , increasing the count to avoid name conflict of immges
        for x in range(0,len(video)):
             hasimage,images=video[x].read()
             cv2.imwrite("Frames/{0}video{1}.jpg".format(x+1,count), images)

    return hasframes[len(hasframes)-1]

#starting from 0th second
sec = 0
#Setting fps , here it will capture image in each 0.5 second , 2fps
frameRate = 0.5
count=1

#to check whether frame are their in video or not.
success = extractframe(sec)
while success:
    #increasing counter to name conflick
    count = count + 1
    #setting sec
    sec = sec + frameRate
    sec = round(sec, 2)
    print(sec)
    success = extractframe(sec)
 
        
