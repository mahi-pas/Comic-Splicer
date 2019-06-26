from tkinter import * 
from tkinter import filedialog
from PIL import ImageTk,Image
from PIL import ImageGrab
import glob, os

class GUI:
    def __init__(self, master):
        self.master = root
        master.title("Comic Splicer")

'''
        #splice button
        self.splice_button=Button(self.master,text="Splice!", command==self.splice)
        self.splice_button.pack()
 
    def splice(self):
        print("splice")
  ''' 
root = Tk()
root.geometry("925x510") #GUI start size
my_gui = GUI(root)
root.mainloop()