#import module from tkinter for UI
from tkinter import *
import cv2
import os
import numpy as np
from PIL import Image
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    #face_id=input('enter your id')
    os.system("datasetcapture.py")
    
    
def function2():
    
    os.system("datasettrainer.py")

def function3():

    os.system("datasetrecognition.py")
    

#def function5():    
   #os.startfile(os.getcwd()+"/developers/diet1frame1first.html");
       #os.system("HospitalManagementSystem.py")
   
#def function6():

    #root.destroy()

#def attend():
    #os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')
    
    

#stting title for the window
root.title("PATIENT RECOGNIITION FOR HOSPITAL")

#creating a text label
Label(root, text="FACE RECOGNITION",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Capture Face",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Add Patient",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize Patient",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#my  new function (see health record)       
#Button(root,text="Health Record",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)       
       
#creating attendance button
#Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#Button(root,text="Developers",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()