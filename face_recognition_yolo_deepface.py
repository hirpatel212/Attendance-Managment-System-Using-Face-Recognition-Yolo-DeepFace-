from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from ultralytics import YOLO
from deepface import DeepFace
import pickle
from db_config import get_connection
import time

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #Title
        title_lbl = Label(self.root, text=" FACE RECOGNITION ",font=("times new roman", 35, "bold"), bg="white", fg="sienna")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        #Image 1
        img_top1 = Image.open("images/facerecignition1.png").resize((700, 750), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        f_lbl2 = Label(self.root, image=self.photoimg_top1)
        f_lbl2.place(x=5, y=55, width=700, height=750)

        #Image 2
        img_bottom = Image.open("images/facerecognition2.png").resize((950, 750), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl3 = Label(self.root, image=self.photoimg_bottom)
        f_lbl3.place(x=700, y=55, width=950, height=750)

        #Button 
        bt1_1 = Button(f_lbl3 , text="Face Recognition", cursor="hand2",command=self.face_recog, font=("times new roman",20, "bold"), bg="gold", fg="black")
        bt1_1.place(x=380, y=680, width=200, height=40)

        # Load trained embeddings
        self.embeddings_dict = None
        self.student_cache = {}  # Cache for student details
        self.load_embeddings()

    def load_embeddings(self):
        """Load pre-trained face embeddings"""
        try:
            if os.path.exists("face_embeddings.pkl"):
                with open("face_embeddings.pkl", "rb") as f:
                    self.embeddings_dict = pickle.load(f)
                print(f"Loaded embeddings for {len(self.embeddings_dict)} students")
            else:
                messagebox.showwarning("Warning", "No trained model found! Please train the model first.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load embeddings: {str(e)}")

    # ============= attendance =======================
    
    def mark_attendance(self,i,r,n,d):
        with open("hmv.csv","r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # ============ face recognition with YOLO + DeepFace ==================

    # ============ OPTIMIZED face recognition with caching ==================

    # ============ IMPROVED face recognition with better accuracy ==================

    def preprocess_face(self, face_img):
        """Preprocess face image for better recognition"""
        # Convert to RGB (DeepFace expects RGB)
        face_rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
        
        # Histogram equalization for better lighting
        face_yuv = cv2.cvtColor(face_img, cv2.COLOR_BGR2YUV)
        face_yuv[:,:,0] = cv2.equalizeHist(face_yuv[:,:,0])
        face_enhanced = cv2.cvtColor(face_yuv, cv2.COLOR_YUV2RGB)
        
        return face_enhanced

    def get_student_details(self, student_id):
        """Get student details with caching to avoid repeated database queries"""
        if student_id in self.student_cache:
            return self.student_cache[student_id]
        
        try:
            conn = get_connection()
            my_cursor = conn.cursor()
            
            my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=%s", (student_id,))
            result = my_cursor.fetchone()
            
            conn.close()
            
            if result:
                details = {
                    'name': result[0],
                    'roll': result[1],
                    'dep': result[2],
                    'id': str(student_id)
                }
                self.student_cache[student_id] = details
                return details
        except:
            pass
        
        return None

    def face_recog(self):
        if self.embeddings_dict is None or len(self.embeddings_dict) == 0:
            messagebox.showerror("Error", "No trained data found! Please train the model first.")
            return

        try:
            # Load YOLO model for face detection
            yolo_model = YOLO('yolov8n-face.pt')
        except:
            try:
                yolo_model = YOLO('yolov8n.pt')
                messagebox.showinfo("Info", "Using general YOLO model.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load YOLO model: {str(e)}")
                return

        video_cap = cv2.VideoCapture(0)
        
        # Set camera properties
        video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        video_cap.set(cv2.CAP_PROP_FPS, 30)
        
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Could not open webcam.")
            return

        print("Face recognition started. Press Enter to exit.")
        print("Tips: Face camera directly, ensure good lighting, stay 1-2 meters away")
        
        # Recognition settings
        frame_skip = 1  # Process every frame for better accuracy
        frame_count = 0
        last_recognition = {}
        recognition_cooldown = 15  # Reduced cooldown for faster re-recognition

        while True:
            ret, frame = video_cap.read()
            if not ret:
                break

            frame_count += 1
            
            # Process every frame for better accuracy
            if frame_count % frame_skip != 0:
                cv2.imshow("Face Recognition System", frame)
                if cv2.waitKey(1) == 13:
                    break
                continue

            # Detect faces using YOLO with lower confidence for better detection
            results = yolo_model(frame, conf=0.3, verbose=False)
            
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
                    # Add padding to face region for better context
                    padding = 20
                    x1 = max(0, x1 - padding)
                    y1 = max(0, y1 - padding)
                    x2 = min(frame.shape[1], x2 + padding)
                    y2 = min(frame.shape[0], y2 + padding)
                    
                    # Extract face region
                    face_img = frame[y1:y2, x1:x2]
                    
                    if face_img.size == 0 or face_img.shape[0] < 50 or face_img.shape[1] < 50:
                        continue
                    
                    # Check if we recently recognized someone in this area
                    face_center = ((x1 + x2) // 2, (y1 + y2) // 2)
                    skip_recognition = False
                    best_match_id = None
                    best_distance = float('inf')
                    
                    for pos, (last_id, last_frame, last_dist) in list(last_recognition.items()):
                        dist = np.sqrt((pos[0] - face_center[0])**2 + (pos[1] - face_center[1])**2)
                        if dist < 100 and (frame_count - last_frame) < recognition_cooldown:
                            # Same person, use cached result
                            best_match_id = last_id
                            best_distance = last_dist
                            skip_recognition = True
                            break
                    
                    if not skip_recognition:
                        try:
                            # Preprocess face for better recognition
                            face_processed = self.preprocess_face(face_img)
                            
                            # Resize for consistent processing
                            face_resized = cv2.resize(face_processed, (160, 160))
                            
                            # Generate embedding - try multiple times for robustness
                            embedding_objs = None
                            for attempt in range(2):  # Try twice
                                try:
                                    embedding_objs = DeepFace.represent(
                                        img_path=face_resized,
                                        model_name="Facenet",
                                        enforce_detection=False,
                                        detector_backend='skip',
                                        align=False  # Disable alignment to avoid TensorFlow errors
                                    )
                                    if embedding_objs:
                                        break
                                except Exception as embed_error:
                                    if attempt == 0:
                                        # Try with original face on second attempt
                                        face_resized = cv2.resize(face_img, (160, 160))
                                    continue
                            
                            if not embedding_objs:
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 165, 255), 2)
                                cv2.putText(frame, "Processing...", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 165, 255), 2)
                                continue
                                
                            current_embedding = np.array(embedding_objs[0]["embedding"])
                            
                            # Find best match with improved threshold
                            best_match_id = None
                            best_distance = float('inf')
                            threshold = 10.0  # Increased threshold for better matching (Euclidean distance)
                            
                            for student_id, embeddings_list in self.embeddings_dict.items():
                                stored_embedding = np.array(embeddings_list[0])
                                
                                # Calculate Euclidean distance
                                distance = np.linalg.norm(current_embedding - stored_embedding)
                                
                                if distance < best_distance:
                                    best_distance = distance
                                    best_match_id = student_id
                            
                            # Cache this recognition
                            if best_match_id and best_distance < threshold:
                                last_recognition[face_center] = (best_match_id, frame_count, best_distance)
                            
                        except Exception as e:
                            print(f"Recognition error: {str(e)}")
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 165, 255), 2)
                            cv2.putText(frame, "Processing...", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 165, 255), 2)
                            continue
                    
                    # Display results
                    if best_match_id and best_distance < 10.0:
                        # Get student details from cache
                        details = self.get_student_details(best_match_id)
                        
                        if details:
                            # Calculate confidence percentage
                            confidence = max(0, min(100, (1 - best_distance / 10.0) * 100))
                            
                            # Draw green rectangle for recognized face
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                            
                            # Display information with better formatting
                            y_offset = y1 - 10
                            cv2.putText(frame, f"ID: {details['id']}", (x1, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                            y_offset -= 25
                            cv2.putText(frame, f"Name: {details['name']}", (x1, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                            y_offset -= 25
                            cv2.putText(frame, f"Roll: {details['roll']}", (x1, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                            y_offset -= 25
                            cv2.putText(frame, f"Dept: {details['dep']}", (x1, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                            
                            # Show confidence
                            cv2.putText(frame, f"Match: {confidence:.1f}%", (x1, y2+25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                            
                            # Mark attendance
                            self.mark_attendance(details['id'], details['roll'], details['name'], details['dep'])
                    else:
                        # Unknown face or low confidence
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                        if best_distance < float('inf'):
                            cv2.putText(frame, f"Unknown ({best_distance:.2f})", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        else:
                            cv2.putText(frame, "Unknown", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            # Clean up old recognitions from cache
            if frame_count % 100 == 0:
                last_recognition = {k: v for k, v in last_recognition.items() 
                                   if (frame_count - v[1]) < recognition_cooldown * 2}

            # Display instructions
            cv2.putText(frame, "Press ENTER to exit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow("Face Recognition System", frame)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        video_cap.release()
        cv2.destroyAllWindows()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
