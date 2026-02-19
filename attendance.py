from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #========variables================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # First image
        img = Image.open("images/studentimg1.jpg").resize((770, 100), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl1 = Label(self.root, image=self.photoimg)
        f_lbl1.place(x=0, y=0, width=770, height=100)

        # Second image
        img1 = Image.open("images/faceimg4.jpg").resize((770, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl2 = Label(self.root, image=self.photoimg1)
        f_lbl2.place(x=770, y=0, width=770, height=100)

 
        # Background image
        img3 = Image.open("images/bgimg1.jpg").resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text=" ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman", 35, "bold"), bg="white", fg="purple")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=620)


        
        # left label frame 
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 15, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=600)

        img_left = Image.open("images/studentimg2.jpg").resize((700, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl1 = Label(Left_frame, image=self.photoimg_left)
        f_lbl1.place(x=5, y=0, width=705, height=120)

        left_inside_frame = Frame(Left_frame,relief=RIDGE, bd=2, bg="white")
        left_inside_frame.place(x=2, y=135, width=710, height=430)

       

        #attendance id 
        attendanceID_label = Label( left_inside_frame, bg="white", text="Attendance ID :", font=("times new roman", 13, "bold"))
        attendanceID_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,font=("times new roman", 13, "bold"), width=20)    
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=10,  sticky=W)

        # roll
        rollLabel = Label( left_inside_frame, bg="white", text="Roll :", font=("times new roman", 13, "bold"))
        rollLabel.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        atten_roll = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,font=("times new roman", 13, "bold"), width=20)    
        atten_roll.grid(row=0, column=3, padx=10, pady=10,  sticky=W)

        # name
        nameLabel = Label( left_inside_frame, bg="white", text="Name :", font=("times new roman", 13, "bold"))
        nameLabel.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        atten_name = ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,font=("times new roman", 13, "bold"), width=20)    
        atten_name.grid(row=1, column=1, padx=10, pady=10,  sticky=W)

        # department
        depLabel = Label( left_inside_frame, bg="white", text="Department :", font=("times new roman", 13, "bold"))
        depLabel.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        atten_dep = ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,font=("times new roman", 13, "bold"), width=20)    
        atten_dep.grid(row=1, column=3, padx=10, pady=10,  sticky=W)

        # time
        timeLabel = Label( left_inside_frame, bg="white", text="Time :", font=("times new roman", 13, "bold"))
        timeLabel.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        atten_time = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,font=("times new roman", 13, "bold"), width=20)    
        atten_time.grid(row=2, column=1, padx=10, pady=10,  sticky=W)

        # date
        dateLabel = Label( left_inside_frame, bg="white", text="Date :", font=("times new roman", 13, "bold"))
        dateLabel.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        atten_date = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,font=("times new roman", 13, "bold"), width=20)    
        atten_date.grid(row=2, column=3, padx=10, pady=10,  sticky=W)

        # attendance
        attendanceLabel = Label( left_inside_frame, bg="white", text="Attendance Status :", font=("times new roman", 13, "bold"))
        attendanceLabel.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman", 13, "bold"), state="readonly" , width=18)
        self.atten_status.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        self.atten_status["values"] = ( "Status", "Present", "Absent")
        self.atten_status.current(0)

        
        # buttons frame 
        
        btn_frame = Frame(left_inside_frame, bd=0, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=250, width=705, height=140)

        import_btn=Button(btn_frame,text="Import csv", command=self.importCsv,width=34,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0, padx=10, pady=10)
        
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=34,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1, padx=10, pady=10)
        
        update_btn=Button(btn_frame,text="Update", width=34,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=0, padx=10, pady=10)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=34,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=1,column=1, padx=10, pady=10)




        # right label frame 
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 15, "bold"))
        Right_frame.place(x=740, y=10, width=720, height=600)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=705, height=560)


        # =============  scroll bar ================

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Atteendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=2)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    #==================================== Fetch Data =========================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END, values=i)

    # import CSV 
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title= "Open CSV", filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
        
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent = self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)                

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()