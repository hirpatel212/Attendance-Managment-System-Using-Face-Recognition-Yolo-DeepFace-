# Setup Instructions for New Users

## 📥 After Cloning from GitHub

### Step 1: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/Attendance-Managment-System-Using-Face-Recognition-Yolo-DeepFace.git
cd Attendance-Managment-System-Using-Face-Recognition-Yolo-DeepFace
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Database
```bash
# Copy the example config
cp db_config_example.py db_config.py

# Edit db_config.py with your MySQL credentials
# Change 'your_password_here' to your actual MySQL password
```

**Windows (PowerShell):**
```powershell
Copy-Item db_config_example.py db_config.py
# Then edit db_config.py
```

### Step 4: Setup Database
```bash
python setup_database.py
```

### Step 5: Create Data Folder
```bash
mkdir data
```

**Windows:**
```cmd
mkdir data
```

### Step 6: Download YOLO Model (Optional)
The system will auto-download `yolov8n.pt` on first run.

For better accuracy, download face-specific model:
- Download: `yolov8n-face.pt` from releases
- Place in project root folder

### Step 7: Run Application
```bash
python main.py
```

---

## 🎯 Quick Start

1. **Add Student** → Fill details → Take 300 photos
2. **Train Model** → Run `python train_stable.py`
3. **Recognition** → Click "Face Detector" → Start recognition
4. **View Attendance** → Click "Attendance" → Import CSV

---

## 📝 Configuration

### Database Settings
Edit `db_config.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'username': 'root',
    'password': 'YOUR_PASSWORD',  # Change this
    'database': 'face_recognizer_yolo'
}
```

### Recognition Threshold
Edit `face_recognition_yolo_deepface.py` (line ~180):
```python
threshold = 10.0  # Increase for looser matching
```

---

## 🐛 Common Issues

### Issue: db_config.py not found
**Solution:** Copy from example
```bash
cp db_config_example.py db_config.py
```

### Issue: data/ folder not found
**Solution:** Create it
```bash
mkdir data
```

### Issue: YOLO model not found
**Solution:** It will auto-download on first run. Wait for it.

### Issue: MySQL connection error
**Solution:** 
1. Check MySQL is running
2. Verify credentials in `db_config.py`
3. Run `python setup_database.py`

---

## 📚 Documentation

- `README.md` - Main documentation
- `QUICK_START.md` - Quick guide
- `RECOGNITION_TROUBLESHOOTING.md` - Fix recognition issues
- `TENSORFLOW_ERROR_FIX.md` - Fix TensorFlow errors

---

## ✅ Verification

After setup, verify:
- [ ] Dependencies installed
- [ ] db_config.py created and configured
- [ ] Database created
- [ ] data/ folder exists
- [ ] Application runs without errors

---

## 🎉 You're Ready!

Start using the system:
```bash
python main.py
```

For detailed instructions, see `README.md`
