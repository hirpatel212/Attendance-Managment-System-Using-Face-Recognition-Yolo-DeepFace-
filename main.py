from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student_yolo import Student
from train_yolo_deepface import Train
from face_recognition_yolo_deepface import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help





class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

      
        # First image
        img = Image.open("images/faceimg1.jpg").resize((520, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl1 = Label(self.root, image=self.photoimg)
        f_lbl1.place(x=0, y=0, width=520, height=130)

        # Second image
        img1 = Image.open("images/aditimg.jpg").resize((525, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl2 = Label(self.root, image=self.photoimg1)
        f_lbl2.place(x=500, y=0, width=525, height=130)

        # Third image
        img2 = Image.open("images/faceimg2.jpg").resize((530, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl3 = Label(self.root, image=self.photoimg2)
        f_lbl3.place(x=1000, y=0, width=530, height=130)

        # Background image
        img3 = Image.open("images/bgimg1.jpg").resize((1530, 910), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=910)

        # Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman", 35, "bold"), bg="aquamarine", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #================== Real time ================= 

        def time():
            String = strftime('%H:%M:%S %p')
            lbl.config(text = String)
            lbl.after(1000, time)
        lbl = Label(bg_img, font=('times new roman',14,'bold'), foreground='black', background="lightyellow")
        lbl.place(x=1417, y=630, width=110, height=30)
        time()


        # student button
        img4 = Image.open("images/studentimg.png").resize((200, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img , image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=200, height=200)

        b1_1 = Button(bg_img , text="Student Details",command=self.student_details, cursor="hand2", font=("times new roman",20, "bold"), bg="lightblue", fg="red")
        b1_1.place(x=200, y=300, width=200, height=40)

        # detect face button
        img5 = Image.open("images/facedetectorimg.png").resize((200, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img , image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=500, y=100, width=200, height=200)

        b1_1 = Button(bg_img , text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman",20, "bold"), bg="lightblue", fg="red")
        b1_1.place(x=500, y=300, width=200, height=40)

        # attendance button
        img6 = Image.open("images/attendanceimg.png").resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img , image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=800, y=100, width=200, height=200)

        b1_1 = Button(bg_img , text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman",20, "bold"), bg="lightblue", fg="red")
        b1_1.place(x=800, y=300, width=200, height=40)

        # help desk button
        img7 = Image.open("images/helpdesk.png").resize((200, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img , image=self.photoimg7, cursor="hand2", command=self.help_data)
        b1.place(x=1100, y=100, width=200, height=200)

        b1_1 = Button(bg_img , text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman",20, "bold"), bg="lightblue", fg="red")
        b1_1.place(x=1100, y=300, width=200, height=40)

        # train face button
        img8 = Image.open("images/traindata.png").resize((200, 200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img , image=self.photoimg8, cursor="hand2", command=self.train_data )
        b1.place(x=200, y=380, width=200, height=200)

        b1_1 = Button(bg_img , text="Train Data", cursor="hand2", command=self.train_data,font=("times new roman",20, "bold"), bg="lightblue", fg="red")
        b1_1.place(x=200, y=580, width=200, height=40)

        # Photos face button
        img9 = Image.open("images/photos.png").resize((200, 200), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img , image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=380, width=200, height=200)

        b1_1 = Button(bg_img , text="Photos", cursor="hand2", command=self.open_img, font=("times new roman",20, "bold"), bg="lightblue", fg="red")
        b1_1.place(x=500, y=580, width=200, height=40)

        # Developer button
        img10 = Image.open("images/developer.png").resize((200, 200), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img , image=self.photoimg10, cursor="hand2",command=self.developer_data )
        b1.place(x=800, y=380, width=200, height=200)

        b1_1 = Button(bg_img , text="Developer", cursor="hand2", command=self.developer_data ,font=("times new roman",20, "bold"), bg="lightblue", fg="red")
        b1_1.place(x=800, y=580, width=200, height=40)

        # Exit button
        img11 = Image.open("images/exit.png").resize((200, 200), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img , image=self.photoimg11, cursor="hand2", command=self.iExit)
        b1.place(x=1100, y=380, width=200, height=200)

        b1_1 = Button(bg_img , text="Exit", cursor="hand2",command=self.iExit, font=("times new roman",20, "bold"), bg="lightblue", fg="red")
        b1_1.place(x=1100, y=580, width=200, height=40)


    #============== Photos button accessing photos ===================

    def open_img(self):
        os.startfile("data")





    def iExit(self):
        self.iExit= tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project ", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


 #===================function button=========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)  
    root.mainloop()














#install pillow library by using  ....    pip install pillow
# pip install opencv-python
# python.exe -m pip install --upgrade pip


# for haar cascade algorithm 
# open python in searchbar then right click and click open file location
# then on python again rightclick and select open file location 
# C:\Users\DELL\AppData\Roaming\Python\Python313\site-packages\cv2\data


# pip install numpy
