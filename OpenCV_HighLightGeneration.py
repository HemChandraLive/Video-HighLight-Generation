#Please go below URL , before going through code
#https://hemchandralive.blogspot.com/2019/10/highlight-creation-with-using-opencv.html

#import Needed Libraries
import cv2
import os 
import glob
from datetime import datetime
from moviepy.editor import VideoFileClip,concatenate_videoclips


#Multi Face Detection Classifier
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#For creating directory hc_videos , if it is not exist . Here our camera feed is saving.
if not os.path.exists("hc_videos"):
        os.makedirs("hc_videos");

#Opening the web camera
video_capture = cv2.VideoCapture(0)

#Defining the codec 
vid_cod = cv2.VideoWriter_fourcc(*'XVID')

#For making video file name on unique timestamp
dateTimeObj=datetime.now()
videoname = dateTimeObj.strftime("%d %b %Y %H %M %S")

#For Checking:print('Current Timestamp : ', videoname)

#Creating VideoWriter object
output = cv2.VideoWriter("hc_videos/{}.mp4".format(videoname), vid_cod, 10.0, (640,480))
      
    
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    #Converting Frame From RGB into Gray 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Setting facedetection parameters
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        currentime=dateTimeObj.strftime("%d %b %Y %H %M %S")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #print(x," ",y," ",w," ",h)
        
        
    #For writing the current time on video
    dateTimeObj1= datetime.now()
    currentime1=dateTimeObj1.strftime("%d %b %Y %H %M %S")    
    cv2.putText(frame,currentime1, (10,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)


   #len(faces) returns 0 , when object is not detected . 
   #Below segment will activate when human face will not detect
    if(len(faces)==0):
        #if face is not detected release the current output file.
        output.release()
        #resetting the parameters
        dateTimeObj=datetime.now()
        videoname = dateTimeObj.strftime("%d %b %Y %H %M %S")
        #print('Current Timestamp : ', videoname)
        output = cv2.VideoWriter("hc_videos/{}.mp4".format(videoname), vid_cod, 10.0, (640,480))
      
    if(len(faces)==1):
        #if face is detecting than write on new file.
         output.write(frame)
        
    # Display the current video feed on screen
    cv2.imshow('Video', frame)

    #on press q , stop the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
output.release()
video_capture.release()
cv2.destroyAllWindows()

#--------------------------------------------------------------------#
#Listing all video files in hc_videos directory
list=glob.glob("hc_videos/*")

#Cleaning unwanted video files
for x in list:    
    try:
        clip = VideoFileClip(x)
    except:
        for i in glob.glob(x):
            os.remove(i)


#Merging Remaining Clips

list=glob.glob("hc_videos/*")
#print(list) For Printing Items in Directory

#Merging all clips into one 
clips = []

for x in list:
    clips.append(VideoFileClip(x))
    
    
final_clip = concatenate_videoclips([x for x in clips])

dateTimeObj=datetime.now()
videoname ="HighligtVideo"+dateTimeObj.strftime("%d %b %Y %H %M %S")
#finally merging all clips into one

#For creating directory Highlight_CV , if it is not exist
if not os.path.exists("Highlight_CV"):
        os.makedirs("Highlight_CV");

#Writing the video files into Highlight_CV Folder
final_clip.write_videofile("Highlight_CV/{}.mp4".format(videoname))
