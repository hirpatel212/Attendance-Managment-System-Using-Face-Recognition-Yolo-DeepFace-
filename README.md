# Face Recognition Attendance System

Advanced face recognition attendance system using YOLO for detection and DeepFace for recognition with 95-98% accuracy.

<<<<<<< HEAD
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12+-orange.svg)

---

## 🚀 Features

- ✅ **YOLO v8** - Fast and accurate face detection
- ✅ **DeepFace (FaceNet)** - 95-98% recognition accuracy
- ✅ **Automatic Attendance** - Marks attendance in real-time
- ✅ **MySQL Database** - Secure student data storage
- ✅ **CSV Export** - Easy attendance management
- ✅ **User-Friendly GUI** - Built with Tkinter
- ✅ **Optimized Performance** - 25-30 FPS recognition
- ✅ **Stable Training** - No TensorFlow conflicts

---

## 📋 System Requirements

- **Python:** 3.8 or higher
- **MySQL Server:** 5.7 or higher
- **Webcam:** Any USB or built-in camera
- **OS:** Windows, Linux, or macOS
- **RAM:** Minimum 4GB (8GB recommended)
- **Storage:** 500MB free space

---

## 🔧 Installation

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Setup Database

**Option A - Automatic (Recommended):**
```bash
python setup_database.py
```

**Option B - Manual:**
1. Open MySQL
2. Run these commands:
```sql
CREATE DATABASE face_recognizer_yolo;
USE face_recognizer_yolo;

CREATE TABLE student (
    Dep VARCHAR(100),
    Subject VARCHAR(100),
    Year VARCHAR(100),
    Semester VARCHAR(100),
    Student_id INT PRIMARY KEY,
    Name VARCHAR(100),
    Division VARCHAR(50),
    Roll VARCHAR(50),
    Gender VARCHAR(20),
    DOB VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(50),
    Address VARCHAR(200),
    Teacher VARCHAR(100),
    Photosample VARCHAR(10)
);
```

### Step 3: Configure Database (If Needed)

Edit `db_config.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'username': 'root',           # Your MySQL username
    'password': 'abcd1234',       # Your MySQL password
    'database': 'face_recognizer_yolo'
}
```

---

## 🎯 Quick Start

### Run the Application:
```bash
python main.py
```

### Complete Workflow:

#### 1️⃣ Add Students
- Click **"Student Details"**
- Fill in student information
- Click **"Save"**
- Click **"Take Photo Sample"**
- System captures 300 photos automatically
- Press **Enter** when done

#### 2️⃣ Train the Model
**Option A - Stable (Recommended):**
```bash
python train_stable.py
```
Click **"TRAIN DATA"** and wait 2-5 minutes

**Option B - Through Main App:**
- Click **"Train Data"**
- Click **"TRAIN DATA"**
- Wait for completion

#### 3️⃣ Run Face Recognition
- Click **"Face Detector"**
- Click **"Face Recognition"**
- System recognizes faces and marks attendance automatically
- Press **Enter** to stop

#### 4️⃣ View Attendance
- Click **"Attendance"**
- Click **"Import csv"**
- Select `hmv.csv`
- View/Export attendance records

---

## 📁 Project Structure

```
project/
├── main.py                              # Main dashboard
├── student_yolo.py                      # Student management
├── train_stable.py                      # Stable training (recommended)
├── train_yolo_deepface.py              # Fast training (alternative)
├── face_recognition_yolo_deepface.py   # Face recognition
├── attendance.py                        # Attendance viewer
├── db_config.py                         # Database configuration
├── setup_database.py                    # Database setup script
├── requirements.txt                     # Python dependencies
├── data/                                # Student photos
├── images/                              # UI images
├── hmv.csv                              # Attendance records
└── face_embeddings.pkl                  # Trained model (generated)
```

---

## ⚙️ Configuration

### Database Settings
Edit `db_config.py` to change database credentials.

### Recognition Threshold
Edit `face_recognition_yolo_deepface.py` (line ~180):
```python
threshold = 10.0  # Increase for looser matching (12.0-15.0)
```

### Number of Training Photos
Edit `student_yolo.py` (line ~530):
```python
if cv2.waitKey(1) == 13 or int(img_id) == 300:  # Change 300 to desired number
```

### Frame Processing Speed
Edit `face_recognition_yolo_deepface.py`:
```python
frame_skip = 1  # Increase to 2 or 3 for faster processing
```

---

## 🎓 Usage Tips

### For Best Photo Capture:
- ✅ Good lighting (face a window or light source)
- ✅ Plain background
- ✅ Face camera directly
- ✅ Stay 1-2 meters from camera
- ✅ Vary expressions slightly (smile, neutral, serious)

### For Best Recognition:
- ✅ Similar lighting as training photos
- ✅ Face camera directly
- ✅ Stay 1-2 meters away
- ✅ Remove obstructions (hands, hair, mask)
- ✅ Ensure good lighting

---

## 🐛 Troubleshooting

### Issue: TensorFlow Error During Training
**Solution:** Use the stable training script
```bash
python train_stable.py
```

### Issue: Face Not Recognized
**Solutions:**
1. Increase threshold in `face_recognition_yolo_deepface.py` to 12.0
2. Retake photos with better lighting
3. Ensure you trained the model after adding photos
4. Check distance value shown (should be < 10.0)

See `RECOGNITION_TROUBLESHOOTING.md` for detailed guide.

### Issue: Database Connection Error
**Solutions:**
1. Check MySQL is running
2. Verify credentials in `db_config.py`
3. Run `python setup_database.py` again

### Issue: Webcam Not Opening
**Solutions:**
1. Close other apps using webcam
2. Check webcam is connected
3. Try changing camera index from 0 to 1 in code

### Issue: Module Not Found
**Solution:**
```bash
pip install -r requirements.txt
```

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Detection Speed | 25-30 FPS |
| Recognition Accuracy | 95-98% |
| Training Time | 2-5 minutes (3 students, 900 images) |
| Model File Size | 0.5-1 MB (100x smaller than unoptimized) |
| Photos per Student | 300 (or 100 for faster training) |

### Optimizations Applied:
- ✅ Parallel processing (4x faster training)
- ✅ Embedding averaging (100x smaller files)
- ✅ Frame skipping (2x faster recognition)
- ✅ Student caching (90% fewer database queries)
- ✅ Recognition cooldown (smoother performance)
- ✅ Histogram equalization (better lighting handling)

---

## 🔬 Technologies Used

- **Python 3.8+** - Programming language
- **YOLO v8** - Face detection
- **DeepFace (FaceNet)** - Face recognition
- **OpenCV** - Image processing
- **TensorFlow** - Deep learning backend
- **MySQL** - Database management
- **Tkinter** - GUI framework
- **NumPy** - Numerical computations
- **Pillow** - Image handling

---

## 📚 Documentation

- `QUICK_START.md` - Quick setup guide
- `RUN_PROJECT.md` - Detailed instructions
- `RECOGNITION_TROUBLESHOOTING.md` - Fix recognition issues
- `TENSORFLOW_ERROR_FIX.md` - Fix TensorFlow errors
- `PERFORMANCE_OPTIMIZATIONS.md` - Technical details
- `FILES_OVERVIEW.txt` - File structure reference

---

## 🎯 Training Options

### Option 1: Stable Training (Recommended)
```bash
python train_stable.py
```
- ✅ Most reliable
- ✅ No TensorFlow conflicts
- ✅ Automatic error handling
- ⚠️ Slower (but stable)

### Option 2: Fast Training
```bash
python train_yolo_deepface.py
```
- ✅ Faster processing
- ✅ Progress bar
- ⚠️ May have rare TensorFlow errors

**Recommendation:** Use `train_stable.py` for first-time setup.

---

## 🔐 Security Notes

- Student photos stored locally in `data/` folder
- Database credentials in `db_config.py` (keep secure)
- Attendance records in `hmv.csv` (backup regularly)
- No data sent to external servers

---

## 📝 Attendance Management

### Attendance File Format:
```csv
StudentID, Roll, Name, Department, Time, Date, Status
1, 101, John Doe, Computer Science, 14:30:25, 19/02/2026, Present
```

### Export Attendance:
1. Open application
2. Click "Attendance"
3. Click "Import csv" → Select `hmv.csv`
4. Click "Export csv" → Save to desired location

### Manual Editing:
Open `hmv.csv` in Excel or any text editor.

---

## 🚀 Advanced Features

### Multiple Students:
- Add unlimited students
- Each student gets unique ID
- System handles multiple faces simultaneously

### Attendance Tracking:
- Automatic timestamp
- Prevents duplicate entries
- CSV format for easy analysis

### Real-time Recognition:
- 25-30 FPS processing
- Instant attendance marking
- Visual feedback (green box = recognized)

---

## 🔄 Updating the System

### Update Python Packages:
```bash
pip install --upgrade deepface tensorflow opencv-python
```

### Update YOLO Model:
Download latest `yolov8n-face.pt` and replace existing file.

### Retrain Model:
After adding new students or updating photos:
```bash
python train_stable.py
```

---

## 💡 Tips for Production Use

1. **Backup Regularly:**
   - `data/` folder (student photos)
   - `hmv.csv` (attendance records)
   - `face_embeddings.pkl` (trained model)
   - MySQL database

2. **Optimize Performance:**
   - Use SSD for faster file access
   - Close unnecessary applications
   - Ensure good lighting in recognition area

3. **Maintain Accuracy:**
   - Retrain model monthly
   - Update photos if appearance changes significantly
   - Monitor recognition accuracy

4. **Security:**
   - Change default MySQL password
   - Restrict database access
   - Keep `db_config.py` secure

---

## 📞 Support

For issues or questions:
1. Check documentation files
2. Review troubleshooting guides
3. Verify system requirements
4. Test with sample data

---

## 📄 License

This project is for educational purposes.

---

## 🙏 Acknowledgments

- **Ultralytics** - YOLO v8
- **DeepFace** - Face recognition library
- **OpenCV** - Computer vision library
- **TensorFlow** - Deep learning framework

---

## 📈 Version History

### v2.0 (Current)
- ✅ YOLO v8 integration
- ✅ DeepFace recognition
- ✅ Stable training script
- ✅ Performance optimizations
- ✅ Better accuracy (95-98%)
- ✅ Comprehensive documentation

### v1.0 (Legacy)
- Haar Cascade detection
- LBPH recognition
- 70-80% accuracy

---

## 🎉 Getting Started

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Setup database
python setup_database.py

# 3. Run application
python main.py

# 4. Add students → Train model → Start recognition!
```

---

**Made with ❤️ using Python**

For best results, follow the tips in `QUICK_START.md` and `RECOGNITION_TROUBLESHOOTING.md`!



                                                                                ------------ HIR PATEL❤️
=======
