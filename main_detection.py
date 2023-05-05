import cv2
import time
import pyglet
import pathlib
import datetime
from tkinter import *
from PIL import Image,ImageTk
#from direction import destroy


def playAudio():

    fp=(pathlib.Path(__file__).parents[1])
    wavefile = str(fp)+'\\audio\\airhorn1.wav'
    player = pyglet.media.Player()
    music = pyglet.media.load(wavefile)
    player.queue(music)
    player.play()
    time.sleep(2)
    return


def sleepTrack(x,y,Image,stri1):
    
    print ('\n')
    #print (x, y)
    dt =  x - y
    print ("Duration of eye closure:"+str(dt))
    frame = Image.copy()
    fp=(pathlib.Path(__file__).parents[1])
    
    if dt > 2:
        
        camera_capture = Image
        playAudio()
        cv2.putText(Image, "Driver is Drowsy", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(Image, "ET=Time Duration of Eye Closure", (210, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(Image, "ET:<2 = Awake   ET:>2 = Drowsy", (10, 60),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.putText(Image, "ET: {:.2f}".format(dt), (10, 90),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print ("Driver is Sleeping")
        y = time.time()
        playAudio()
        playAudio()
        filea = str(fp)+"\\sleep_images\\sleep_image_"+str(stri1)+".jpg"
        cv2.imwrite(filea, camera_capture)
        playAudio()
        
    else:
        
        cv2.putText(Image, "Driver Awake", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(Image, "ET=Time Duration of Eye Closure", (210, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(Image, "ET:<2 = Awake   ET:>2 = Drowsy", (10, 60),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.putText(Image, "ET: {:.2f}".format(dt), (10, 90),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print ("Driver is Not Sleeping")
    
    return y




    
fp=(pathlib.Path(__file__).parents[1])
init = str(fp)+'\\audio\\initialise.wav'
player = pyglet.media.Player()
music = pyglet.media.load(init)
print ('Initializing the system.....')
player.queue(music)
player.play()
time.sleep(2)
stri = ''

init1 = str(fp)+'\\audio\\running.wav'
player = pyglet.media.Player()
music = pyglet.media.load(init1)
print ('Initializing Completed. System is Running')
player.queue(music)
player.play()
print ('\n')

    
root=Tk()
root.title("SDS")
root.geometry("720x640")
root.configure(bg="black")
Label(root,text="Sleep Detection System",font=("times new roman",30,"bold"),bg="black",fg="white").pack()
f1=LabelFrame(root,bg="blue")
f1.pack()
L1=Label(f1,bg="blue")
L1.pack()
exit_button=Button(root, text="STOP Detection", command=root.destroy)
exit_button.pack(pady=20)

newTime = time.time()
oldTime = time.time()
command = ""


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(str(fp)+'\\haarcascade\\haar-face.xml')
eye_cascade = cv2.CascadeClassifier(str(fp)+'\\haarcascade\\haar-eyes.xml')

while True:
                ret, img = cap.read()

                if ret:

                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.4, 5)

                    for (x,y,w,h) in faces:

                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                        roi_gray = gray[y:y+h, x:x+w]
                        roi_color = img[y:y+h, x:x+w]
                        eyes = eye_cascade.detectMultiScale(roi_gray)
                        newTime = time.time()
                        day = datetime.datetime.now()
                        stri = day.strftime("%I_%M_%S_%p_%d_%m_%Y")
                        oldTime = sleepTrack(newTime,oldTime,img,stri)

                        for (ex,ey,ew,eh) in eyes:

                            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                            newTime = time.time()
                            oldTime = newTime


                    img1= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                    img=ImageTk.PhotoImage(Image.fromarray(img1))
                    L1['image']=img
                    root.update()


cap.release()
cv2.destroyAllWindows()






