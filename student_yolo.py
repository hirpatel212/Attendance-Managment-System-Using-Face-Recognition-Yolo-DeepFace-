from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
from ultralytics import YOLO
from db_config import get_connection

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #===========variables==============
        self.var_dep=StringVar()
        self.var_subject=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_student_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()

        # First image
        img = Image.open("images/faceimg3.png").resize((520, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl1 = Label(self.root, image=self.photoimg)
        f_lbl1.place(x=0, y=0, width=520, height=130)

        # Second image
        img1 = Image.open("images/aditimg2.jpg").resize((525, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl2 = Label(self.root, image=self.photoimg1)
        f_lbl2.place(x=500, y=0, width=525, height=130)

        # Third image
        img2 = Image.open("images/faceimg4.jpg").resize((530, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl3 = Label(self.root, image=self.photoimg2)
        f_lbl3.place(x=1000, y=0, width=530, height=130)

        # Background image
        img3 = Image.open("images/bgimg2.jpg").resize((1530, 910), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=910)

        # Title
        title_lbl = Label(bg_img, text=" STUDENT MANAGEMENT SYSTEM ",font=("times new roman", 35, "bold"), bg="white", fg="purple")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=40, width=1530, height=910)

        # left label frame 
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 15, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=600)

        img_left = Image.open("images/studentimg1.jpg").resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl1 = Label(Left_frame, image=self.photoimg_left)
        f_lbl1.place(x=5, y=0, width=715, height=130)

        # current course 
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course", font=("times new roman", 13, "bold"))
        current_course_frame.place(x=5, y=135, width=715, height=115)

        # Department
        dep_label = Label(current_course_frame,bg="white", text="Department", font=("times new roman", 13, "bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
 
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 13, "bold"), state="readonly", width=20 )
        dep_combo["values"] = ("Select Department", "AIDS", "IT", "FPT", "CSD", "ME")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

         # Subject
        sub_label = Label(current_course_frame,bg="white", text="Subject", font=("times new roman", 13, "bold"))
        sub_label.grid(row=0, column=2, padx=10, sticky=W)
 
        sub_combo = ttk.Combobox(current_course_frame, textvariable=self.var_subject,font=("times new roman", 13, "bold"), state="readonly", width=20 )
        sub_combo["values"] = ("Select Subject", "DAA", "SE", "DS", "CVIP", "SCPM")
        sub_combo.current(0)
        sub_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame,bg="white", text="Year", font=("times new roman", 13, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)
 
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("times new roman", 13, "bold"), state="readonly" , width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame,bg="white", text="Semester", font=("times new roman", 13, "bold"))
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
 
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly", width=20 )
        semester_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

         # class student Information 
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 13, "bold"))
        class_student_frame.place(x=5, y=250, width=715, height=300)

        #student id 
        studentID_label = Label( class_student_frame, bg="white", text="Student ID :", font=("times new roman", 13, "bold"))
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id,font=("times new roman", 13, "bold"), width=20)    
        studentID_entry.grid(row=0, column=1, padx=10, pady=5,  sticky=W)

        #student Name 
        studentName_label = Label( class_student_frame, bg="white", text="Student Name :", font=("times new roman", 13, "bold"))
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_student_name,font=("times new roman", 13, "bold"), width=20)    
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #class division 
        class_div_label = Label( class_student_frame, bg="white", text="Class Division :", font=("times new roman", 13, "bold"))
        class_div_label.grid(row=1, column=0, padx=10, pady=5 ,sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div,font=("times new roman", 13, "bold"), state="readonly" , width=20)
        div_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)
        div_combo["values"] = ("Select Division", "A", "B", "C")
        div_combo.current(0)

        #Roll number s
        roll_no_label = Label( class_student_frame, bg="white", text="Roll no :", font=("times new roman", 13, "bold"))
        roll_no_label.grid(row=1, column=2, padx=10, pady=5 ,sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, font=("times new roman", 13, "bold"), width=20)    
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5,  sticky=W)

        #Gender
        gender_label = Label( class_student_frame, bg="white", text="Gender :", font=("times new roman", 13, "bold"))
        gender_label.grid(row=2, column=0, padx=10, pady=5 ,sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,font=("times new roman", 13, "bold"), state="readonly" , width=20)
        gender_combo.grid(row=2, column=1, padx=2, pady=5, sticky=W)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)

        #DOB
        dob_label = Label( class_student_frame, bg="white", text="DOB :", font=("times new roman", 13, "bold"))
        dob_label.grid(row=2, column=2, padx=10, pady=5 ,sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, font=("times new roman", 13, "bold"), width=20)    
        dob_entry.grid(row=2, column=3, padx=10, pady=5,  sticky=W)

        #Email
        email_label = Label( class_student_frame, bg="white", text="Email :", font=("times new roman", 13, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=5 ,sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, font=("times new roman", 13, "bold"), width=20)    
        email_entry.grid(row=3, column=1, padx=10, pady=5,  sticky=W)

        #Phone number
        phone_label = Label( class_student_frame, bg="white", text="Phone Number :", font=("times new roman", 13, "bold"))
        phone_label.grid(row=3, column=2, padx=10, pady=5 ,sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, font=("times new roman", 13, "bold"), width=20)    
        phone_entry.grid(row=3, column=3, padx=10, pady=5,  sticky=W)

        #Address
        address_label = Label( class_student_frame, bg="white", text="Address :", font=("times new roman", 13, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5 ,sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, font=("times new roman", 13, "bold"), width=20)    
        address_entry.grid(row=4, column=1, padx=10, pady=5,  sticky=W)

        #Teacher name
        teacher_label = Label( class_student_frame, bg="white", text="Teacher Name :", font=("times new roman", 13, "bold"))
        teacher_label.grid(row=4, column=2, padx=10, pady=5 ,sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, font=("times new roman", 13, "bold"), width=20)    
        teacher_entry.grid(row=4, column=3, padx=10, pady=5,  sticky=W)

        # radio  butttons
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=7, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=7, column=1)

        # buttons frame 
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=705, height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        # buttons frame 2
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=240, width=705, height=35)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample", command=self.generate_dataset,width=34,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)
      
        update_photo_btn=Button(btn_frame1,text="Update Photo button",width=34,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

        # right label frame 
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 15, "bold"))
        Right_frame.place(x=750, y=10, width=750, height=600)

        img_right = Image.open("images/studentimg2.jpg").resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl1 = Label(Right_frame, image=self.photoimg_right)
        f_lbl1.place(x=5, y=0, width=730, height=130)

        #search System
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search ", font=("times new roman", 13, "bold"))
        Search_frame.place(x=5, y=135, width=730, height=70)

        search_label = Label( Search_frame, bg="aqua",fg='black', text="Search By :", font=("times new roman", 15, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=5 ,sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15 )
        search_combo["values"] = ("Select", "Roll no", "Phone no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, font=("times new roman", 13, "bold"), width=15)    
        search_entry.grid(row=0, column=2, padx=10, pady=5,  sticky=W)
 
        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(Search_frame,text="ShowAll",width=12,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=730, height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","subject","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("subject",text="Subject")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("subject",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=150)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=150)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    #==================function decration=================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:   
                conn=get_connection()            
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_subject.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_student_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=get_connection()
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_subject.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_student_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),


    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update= messagebox.askyesno("Update","Do you want to update this student details", parent=self.root)
                if Update>0:
                    conn=get_connection()            
                    my_cursor=conn.cursor()
                    my_cursor.execute("""UPDATE student SET Dep=%s, Subject=%s, Year=%s, Semester=%s, Student_id=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photosample=%s WHERE Student_id=%s""",(
                        self.var_dep.get(),
                        self.var_subject.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_student_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated ", parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student", parent=self.root)
                if Delete>0:
                    conn=get_connection()            
                    my_cursor=conn.cursor()
                    sql = "DELETE FROM student WHERE Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()  
                messagebox.showinfo("Delete","Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_subject.set("Select Subject"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_student_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #================= Generate dataset with YOLO ======================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=get_connection()            
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id +=1
                my_cursor.execute("""UPDATE student SET Dep=%s, Subject=%s, Year=%s, Semester=%s, Student_id=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photosample=%s WHERE Student_id=%s""",(
                    self.var_dep.get(),
                    self.var_subject.get(),
                    self.var_semester.get(),
                    self.var_year.get(),
                    self.var_std_id.get(),
                    self.var_student_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() == id+1
                ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load YOLO model for face detection
                try:
                    yolo_model = YOLO('yolov8n-face.pt')
                except:
                    yolo_model = YOLO('yolov8n.pt')
                    messagebox.showinfo("Info", "Using general YOLO. For better results, download yolov8n-face.pt")

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        break
                    
                    # Detect faces using YOLO
                    results = yolo_model(my_frame, conf=0.5, verbose=False)
                    
                    for result in results:
                        boxes = result.boxes
                        for box in boxes:
                            # Get bounding box coordinates
                            x1, y1, x2, y2 = map(int, box.xyxy[0])
                            
                            # Extract and save face
                            face_cropped = my_frame[y1:y2, x1:x2]
                            
                            if face_cropped.size > 0:
                                img_id += 1
                                face = cv2.resize(face_cropped, (450, 450))
                                face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                                file_name_path = f"data/user.{id}.{img_id}.jpg"
                                cv2.imwrite(file_name_path, face_gray)
                                
                                # Display with counter
                                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                                cv2.rectangle(my_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                                cv2.putText(my_frame, f"Captured: {img_id}/300", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    
                    cv2.imshow("YOLO Face Capture", my_frame)

                    if cv2.waitKey(1) == 13 or int(img_id) == 300:
                        break
                        
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", f"Dataset generation completed! Captured {img_id} images.")
                
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
