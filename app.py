from tkinter import * 
from tkinter import scrolledtext
from tkinter import filedialog
from PIL import ImageTk,Image
from PIL import ImageGrab
import glob, os
import pyperclip

def resize_img():
    size = 500, 500 #Thumbnail size
    #makes thumbnail of input.png, which makes it resize correctly for this. input.thumbnail only used for GUI
    for infile in glob.glob("*.png"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + ".thumbnail", "PNG")

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Easy Comic Splicer")

        #Left frame, contains canvas
        self.left_side = Frame(root)
        self.left_side.pack(fill='both', expand='yes')
        self.left_side.place(x=0,y=0)

        #Right frame, contains everything else
        self.right_side = Frame(root)
        self.right_side.pack(fill='both',expand='yes')
        self.right_side.place(x=500,y=0)

        #Canvas click event(gets file opener)
        def click(event):
            file_path = filedialog.askopenfilename()
            im = Image.open(file_path)
            im.save("input.png","PNG")
            resize_img()
            self.input_image=ImageTk.PhotoImage(Image.open("input.thumbnail"))
            self.image = self.image_view.create_image(0, 0, anchor=NW, image=self.input_image)

        #Canvas
        self.input_image=ImageTk.PhotoImage(Image.open("input.thumbnail")) #Image input file
        self.image_view = Canvas(self.left_side, width=500, height=500)
        self.image_view.bind('<Button-1>', click) #Bind click function to canvas
        self.image = self.image_view.create_image(0, 0, anchor=NW, image=self.input_image)
        self.master.bind('<Control-v>', self.paste())
        self.image_view.pack()

        #image width and height
        
        #convert button
        self.convert_button = Button(self.right_side, text="Convert", command=self.convert)
        self.convert_button.pack()



    #fuction for convert button
    def convert(self):
        print("convert")

root = Tk()
root.geometry("925x510") #GUI start size
my_gui = GUI(root)
root.mainloop()