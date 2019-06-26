from tkinter import * 
from tkinter import filedialog
from PIL import ImageTk,Image
from PIL import ImageGrab
import glob, os

class GUI:
    def __init__(self, master):

root = Tk()
root.geometry("925x510") #GUI start size
my_gui = GUI(root)
root.mainloop()