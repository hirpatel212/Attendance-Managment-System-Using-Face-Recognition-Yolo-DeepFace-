# Switch to New GitHub Repository

## Unlink Old Repository and Connect to New One

---

## Step 1: Check Current Remote

```bash
git remote -v
```

This shows your current repository connection.

---

## Step 2: Remove Old Remote

```bash
git remote remove origin
```

This unlinks your project from the old repository.

---

## Step 3: Add New Repository

Replace `YOUR_USERNAME` and `NEW_REPO_NAME` with your actual values:

```bash
git remote add origin https://github.com/YOUR_USERNAME/NEW_REPO_NAME.git
```

**Example:**
```bash
git remote add origin https://github.com/john123/Face-Recognition-Attendance-System.git
```

---

## Step 4: Verify New Remote

```bash
git remote -v
```

Should show your new repository URL.

---

## Step 5: Add All Files

```bash
git add .
```

---

## Step 6: Commit Changes

```bash
git commit -m "Initial commit: Face Recognition Attendance System with YOLO + DeepFace"
```

---

## Step 7: Set Branch Name

```bash
git branch -M main
```

---

## Step 8: Push to New Repository

```bash
git push -u origin main
```

If you get an error about existing content:
```bash
git push -u origin main --force
```

---

## 🎯 Complete Command Sequence

Copy and paste these commands one by one:

```bash
# 1. Remove old remote
git remote remove origin

# 2. Add new remote (CHANGE THE URL!)
git remote add origin https://github.com/YOUR_USERNAME/NEW_REPO_NAME.git

# 3. Verify
git remote -v

# 4. Add files
git add .

# 5. Commit
git commit -m "Initial commit: Face Recognition Attendance System"

# 6. Set branch
git branch -M main

# 7. Push
git push -u origin main
```

---

## 🚀 Quick One-Liner

Replace the URL with your new repository:

```bash
git remote remove origin && git remote add origin https://github.com/YOUR_USERNAME/NEW_REPO_NAME.git && git add . && git commit -m "Initial commit" && git branch -M main && git push -u origin main
```

---

## ⚠️ Important Notes

### 1. Create New Repository First
Before running these commands:
1. Go to GitHub
2. Click "New Repository"
3. Enter repository name
4. Don't initialize with README (we already have one)
5. Click "Create Repository"
6. Copy the repository URL

### 2. Repository URL Format
```
https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
```

### 3. If Push Fails
If you get "failed to push" error:
```bash
git push -u origin main --force
```

---

## 🔍 Troubleshooting

### Error: "remote origin already exists"
```bash
git remote remove origin
# Then add new remote again
```

### Error: "authentication failed"
Use Personal Access Token:
1. GitHub Settings → Developer settings → Personal access tokens
2. Generate new token
3. Use token as password when pushing

### Error: "repository not found"
- Check repository URL is correct
- Ensure repository exists on GitHub
- Verify you have access to the repository

---

## ✅ Verification

After pushing, verify:
1. Go to your new repository URL
2. Check files are uploaded
3. Verify README.md displays correctly
4. Check all documentation files are present

---

## 📝 Example

If your new repository is:
```
https://github.com/john123/Face-Recognition-System
```

Commands would be:
```bash
git remote remove origin
git remote add origin https://github.com/john123/Face-Recognition-System.git
git add .
git commit -m "Initial commit: Face Recognition System"
git branch -M main
git push -u origin main
```

---

## 🎉 Success!

Your project is now connected to the new repository!

Share your new repository:
```
https://github.com/YOUR_USERNAME/NEW_REPO_NAME
```

---

## 🔄 Future Updates

After initial push, for future updates:
```bash
git add .
git commit -m "Update: description of changes"
git push
```

---

## 📋 Quick Reference

```bash
# Check current remote
git remote -v

# Remove remote
git remote remove origin

# Add new remote
git remote add origin URL

# Push to new repo
git push -u origin main
```

---

Good luck with your new repository! 🚀
