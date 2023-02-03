import tkinter as tk
from tkinter import ttk
import cv2

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
        cap = cv2.VideoCapture(0, cv2.CAP_V4L)
                
        while True:
            ret, frame = cap.read()

            cv2.imshow('frame',frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

root = tk.Tk()
app = App(master=root)
app.mainloop()
