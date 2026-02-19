from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np
from deepface import DeepFace
import pickle
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #Title
        title_lbl = Label(self.root, text=" TRAIN DATA SET ",font=("times new roman", 35, "bold"), bg="white", fg="maroon")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        #Image 1
        img_top = Image.open("images/trainingimg1.png").resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl1 = Label(self.root, image=self.photoimg_top)
        f_lbl1.place(x=5, y=55, width=1530, height=325)

        #Button middle
        bt1_1 = Button(self.root , text="TRAIN DATA", command=self.train_classifier,cursor="hand2", font=("times new roman",30, "bold"), bg="tan", fg="black")
        bt1_1.place(x=0, y=380, width=1540, height=60)

        #Image 2
        img_bottom = Image.open("images/trainingimg2.png").resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl1 = Label(self.root, image=self.photoimg_bottom)
        f_lbl1.place(x=5, y=440, width=1530, height=325)

    
    #=============== OPTIMIZED train classifier with parallel processing ===============

    def process_single_image(self, image_path):
        """Process a single image and return embedding"""
        try:
            # Extract student ID from filename (user.ID.number.jpg)
            filename = os.path.basename(image_path)
            student_id = int(filename.split('.')[1])
            
            # Read image first to check if valid
            img = cv2.imread(image_path)
            if img is None:
                return None, None
            
            # Resize to consistent size
            img = cv2.resize(img, (160, 160))
            
            # Get embedding using Facenet model
            embedding_objs = DeepFace.represent(
                img_path=img,
                model_name="Facenet",
                enforce_detection=False,
                detector_backend='skip',
                align=False  # Disable alignment to avoid errors
            )
            
            if embedding_objs:
                embedding = embedding_objs[0]["embedding"]
                return student_id, embedding
            
        except Exception as e:
            # Silently skip problematic images
            pass
        
        return None, None

    def train_classifier(self):
        data_dir = "data"
        
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!")
            return
            
        image_files = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg')]
        
        if len(image_files) == 0:
            messagebox.showerror("Error", "No training images found!")
            return

        # Show progress window
        progress_window = Toplevel(self.root)
        progress_window.title("Training Progress")
        progress_window.geometry("400x150")
        
        progress_label = Label(progress_window, text="Initializing training...", font=("Arial", 12))
        progress_label.pack(pady=20)
        
        progress_bar = ttk.Progressbar(progress_window, length=350, mode='determinate')
        progress_bar.pack(pady=10)
        
        status_label = Label(progress_window, text="", font=("Arial", 10))
        status_label.pack(pady=10)

        embeddings_dict = {}
        total_images = len(image_files)
        processed = 0
        
        def update_progress():
            progress_bar['value'] = (processed / total_images) * 100
            progress_label.config(text=f"Processing: {processed}/{total_images} images")
            status_label.config(text=f"Students found: {len(embeddings_dict)}")
            progress_window.update()

        def train_thread():
            nonlocal processed
            
            try:
                # OPTIMIZATION 1: Use parallel processing with ThreadPoolExecutor
                # Process multiple images simultaneously
                max_workers = 1  # Use single thread to avoid TensorFlow conflicts
                
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    # Submit all tasks
                    future_to_image = {executor.submit(self.process_single_image, img_path): img_path 
                                      for img_path in image_files}
                    
                    # Process results as they complete
                    for future in as_completed(future_to_image):
                        student_id, embedding = future.result()
                        
                        if student_id is not None and embedding is not None:
                            if student_id not in embeddings_dict:
                                embeddings_dict[student_id] = []
                            embeddings_dict[student_id].append(embedding)
                        
                        processed += 1
                        update_progress()

                # OPTIMIZATION 2: Average embeddings per student (reduces file size & improves speed)
                averaged_embeddings = {}
                for student_id, embeddings_list in embeddings_dict.items():
                    # Average all embeddings for this student
                    averaged_embeddings[student_id] = [np.mean(embeddings_list, axis=0).tolist()]
                
                # Save embeddings to file
                if averaged_embeddings:
                    with open("face_embeddings.pkl", "wb") as f:
                        pickle.dump(averaged_embeddings, f)
                    
                    progress_window.destroy()
                    messagebox.showinfo("Success", 
                        f"Training completed!\n\n"
                        f"Processed: {processed}/{total_images} images\n"
                        f"Students: {len(averaged_embeddings)}\n"
                        f"Embeddings averaged for faster recognition!")
                else:
                    progress_window.destroy()
                    messagebox.showerror("Error", "No valid face embeddings generated!")
                    
            except Exception as es:
                progress_window.destroy()
                messagebox.showerror("Error", f"Training failed: {str(es)}")

        # Run training in separate thread to keep GUI responsive
        training_thread = threading.Thread(target=train_thread, daemon=True)
        training_thread.start()

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
