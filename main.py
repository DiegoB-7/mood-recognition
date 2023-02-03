import tkinter as tk
from tkinter import ttk
import cv2 as cv
import numpy as np

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
        cap = cv.VideoCapture(1)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # Display the resulting frame
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                break

root = tk.Tk()
app = App(master=root)
app.mainloop()
