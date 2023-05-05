from tkinter import *
import subprocess
import os
#from final import count

def direction():
    os.chdir(r'c:\Users\Narendra kumar\OneDrive\Documents\Project Driver Drowsiness Detection\Project Driver Drowsiness Detection\Code')
    cmmd1="python main_detection.py"
    p1=subprocess.Popen(cmmd1, shell=True)

t=Tk()

t.title("DDD")
t.geometry('360x240')
t.configure(bg="black")
Label(t,text="Sleep Detection System",font=("times new roman",24,"bold"),bg="black",fg="white").pack()
s1=Button(t, text="Start Detection", command=direction)
s1.pack(side= TOP, padx=30, pady= 0)
buttonQuit=Button(t, text="Exit", command=t.destroy)
buttonQuit.pack(side= TOP, padx=30, pady= 20)
#buttonQuit.pack(side= BOTTOM)

t.mainloop()
