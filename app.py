from tkinter import * 
from tkinter import scrolledtext
from tkinter import filedialog
from PIL import ImageTk,Image
import glob, os


pad = 6 #pushes down interacting UI

#reload initial input image
im = Image.open("res/input.png")
im.save("input.png","PNG")

class GUI:
    def __init__(self, master):
        self.resize()
        self.master = master
        master.title("Easy Comic Splicer")

        #Left frame, contains canvas
        self.left_side = Frame(root)
        self.left_side.pack(fill='both', expand='yes')
        self.left_side.place(x=0,y=0)

        #Right frame, contains everything else
        self.right_side = Frame(root)
        self.right_side.pack(fill='both',expand='yes')
        self.right_side.place(x=250,y=0)

        #Canvas click event(gets file opener)
        def click(event):
            file_path = filedialog.askopenfilename()
            im = Image.open(file_path)
            im.save("input.png","PNG")
            self.resize()
            self.input_image=ImageTk.PhotoImage(Image.open("thumbnail.png"))
            self.image = self.image_view.create_image(0, 0, anchor=NW, image=self.input_image)

        #Canvas
        self.input_image=ImageTk.PhotoImage(Image.open("thumbnail.png")) #Image input file
        self.image_view = Canvas(self.left_side, width=250, height=500)
        self.image_view.bind('<Button-1>', click) #Bind click function to canvas
        self.image = self.image_view.create_image(0, 0, anchor=NW, image=self.input_image)
        self.image_view.pack()

        #image width and height input
        Label(self.right_side, text="Width").grid(row=0+pad)
        Label(self.right_side, text="Height").grid(row=1+pad)

        #entry box
        self.width_input = Entry(self.right_side)
        self.height_input = Entry(self.right_side)
        #default values
        self.width_input.insert(0,"800")
        self.height_input.insert(0,"1280")

        self.width_input.grid(row=0+pad, column=1)
        self.height_input.grid(row=1+pad, column=1)


        #convert button
        self.splice_button = Button(self.right_side, text="Splice!", command=self.splice)
        self.splice_button.grid(row=2+pad, column=1)



    #fuction for convert button
    def splice(self):
        print("splice")
        #get output dir
        output_path = filedialog.askdirectory()

    #resize function
    def resize(self):
        size= 250,500
        im = Image.open("input.png")
        im.thumbnail(size)
        im.save("thumbnail.png", "PNG")


root = Tk()
root.geometry("465x510") #GUI start size
my_gui = GUI(root)
root.mainloop()