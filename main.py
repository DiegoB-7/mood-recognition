import tkinter as tk
from tkinter import ttk
import cv2 
import numpy as np
import sys

class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.start_button = ttk.Button(self, text="Start Camera", command=self.start_camera)
        self.start_button.pack()
        
        self.quit = ttk.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()
        
    def start_camera(self):
        cascPath = sys.argv[1]
        faceCascade = cv2.CascadeClassifier(cascPath)

        video_capture = cv2.VideoCapture(1) 

        while True:
        # Capture frame-by-frame
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

root = tk.Tk()
app = App(master=root)
app.mainloop()
