from tkinter import * 
from tkinter import scrolledtext
from tkinter import filedialog
from PIL import ImageTk,Image
import glob, os


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
            self.image = self.image_view.create_image(0, 0, anchor=NW, image=self.input_image)

        #Canvas
        self.input_image=ImageTk.PhotoImage(Image.open("input.png")) #Image input file
        self.image_view = Canvas(self.left_side, width=500, height=500)
        self.image_view.bind('<Button-1>', click) #Bind click function to canvas
        self.image = self.image_view.create_image(0, 0, anchor=NW, image=self.input_image)
        self.image_view.pack()

        #image width and height input
        Label(self.right_side, text="Width").grid(row=0)
        Label(self.right_side, text="Height").grid(row=1)

        self.width_input = Entry(self.right_side)
        self.height_input = Entry(self.right_side)

        self.width_input.grid(row=0, column=1)
        self.height_input.grid(row=1, column=1)

        #change output path button
        self.dir_button= Button(self.right_side, text="change output directory",command=self.dir_change)
        self.dir_button.grid(row=2,column=1)

        #convert button
        self.splice_button = Button(self.right_side, text="Splice!", command=self.splice)
        self.splice_button.grid(row=3, column=1)



    #fuction for convert button
    def splice(self):
        print("splice")
    
    #func for output path button
    def dir_change(self):
        print("dir change")


root = Tk()
root.geometry("730x510") #GUI start size
my_gui = GUI(root)
root.mainloop()