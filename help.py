from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

         
        #Title
        title_lbl = Label(self.root, text="Help Desk",font=("times new roman", 35, "bold"), bg="aliceblue", fg="maroon")
        title_lbl.place(x=0, y=0,width=1530,height=50)

        #Image 1
        img_top = Image.open("images/helpdeskBG.png").resize((1530, 580), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        

        f_lbl1 = Label(self.root, image=self.photoimg_top, bg="white")
        f_lbl1.place(x=5, y=50, width=1530, height=580)

        #Frame
        img_top2 = Image.open("images/devBG.jpeg").resize((1530, 300), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        f_lbl2 = Label(self.root, image=self.photoimg_top2)
        f_lbl2.place(x=5, y=600, width=1530, height=300)

        main_frame = Frame(f_lbl2, bd=2, bg="AliceBlue")
        main_frame.place(x=0, y=0, width=1530, height=300)

        dev_label=Label(main_frame,text="Reach us on: ",font=("times new roman",20,"bold"),bg="aliceblue")
        dev_label.place(x=680,y=10)

        dev_label=Label(main_frame,text="Name: Hir Patel                                           ",font=("times new roman",20,"bold"),bg="aliceblue")
        dev_label.place(x=120,y=50)

        dev_label=Label(main_frame,text="Email: 12202120601022@adit.ac.in             ",font=("times new roman",20,"bold"),bg="aliceblue")
        dev_label.place(x=120,y=90)

        dev_label=Label(main_frame,text="Contact: 9925166734                                       ",font=("times new roman",20,"bold"),bg="aliceblue")
        dev_label.place(x=120,y=130)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()