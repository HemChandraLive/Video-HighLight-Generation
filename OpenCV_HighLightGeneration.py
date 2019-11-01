#import OpenCv Library
import cv2
import os 
import glob

#HaarCascade Classifier 
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#For Changing the video Name

#Opening the camera
video_capture = cv2.VideoCapture(0)

#For Writing the video file
vid_cod = cv2.VideoWriter_fourcc(*'XVID')

#For making video file name on timestamp 
from datetime import datetime
dateTimeObj=datetime.now()

#Setting the video filename
videoname = dateTimeObj.strftime("%d %b %Y %H %M %S")
print('Current Timestamp : ', videoname)

#Here We are saving our all clips into hc_videos name folder
output = cv2.VideoWriter("hc_videos/{}.mp4".format(videoname), vid_cod, 10.0, (640,480))
      
    
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    #Converting Frame From RGB into Gray 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Setting face parameter
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(x," ",y," ",w," ",h)
  
   
   
   #Below segment will activate when human face will not detect
    if(len(faces)==0):
        output.release()
        dateTimeObj=datetime.now()
        videoname = dateTimeObj.strftime("%d %b %Y %H %M %S")
        print('Current Timestamp : ', videoname)
        output = cv2.VideoWriter("hc_videos/{}.mp4".format(videoname), vid_cod, 10.0, (640,480))
      
    if(len(faces)==1):
         output.write(frame)
        
    # Display the resulting frame
    cv2.imshow('Video', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
output.release()
video_capture.release()
cv2.destroyAllWindows()




from moviepy.editor import VideoFileClip,concatenate_videoclips

list=glob.glob("hc_videos/*")
print(list)

for x in list:    
    try:
        clip = VideoFileClip(x)
    except:
        for i in glob.glob(x):
            os.remove(i)


#Merging Clips

list=glob.glob("hc_videos/*")
print(list)

#Merging all clips into one 
clips = []

for x in list:
    clips.append(VideoFileClip(x))
    

    
final_clip = concatenate_videoclips([x for x in clips])

dateTimeObj=datetime.now()
videoname ="HighligtVideo"+dateTimeObj.strftime("%d %b %Y %H %M %S")
#finally merging all clips into one
final_clip.write_videofile("Highlight_CV/{}.mp4".format(videoname))
