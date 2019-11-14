#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:47:58 2019
@author: Jo
"""
#Doing with open cv2
#Import Cv2 library
import cv2,os
from moviepy.editor import VideoFileClip

inputfilepath="Dataset/vid1.mov"

#For saving output   
if not os.path.exists('Frames'):
    os.makedirs('Frames')

#location of video file
video=cv2.VideoCapture(inputfilepath)

#For Getting Clip duration
clip = VideoFileClip(inputfilepath)
print(clip.duration,"seconds")

def extractframe(sec):
    # cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000) is responsible for 
    #skipping directly to the sec in the video (sec*1000th millisecond)
    video.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
    #reading frame
    hasframes,image = video.read()
         
    if hasframes:
        #Write to location , increasing the count to avoid name conflict of iamges
        #
        cv2.imwrite("Frames/image"+str(count)+".jpg", image)  # save frame as JPG file
        
    return hasframes

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
 
        
