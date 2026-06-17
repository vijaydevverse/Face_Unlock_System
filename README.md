# 🔐 Face Unlock System

An AI-powered facial authentication system built with Python, OpenCV, and Face Recognition. This project enables secure user verification through real-time face detection and matching using a webcam. The system registers a user's face and grants access only when a matching face is detected during authentication.

---

## 📌 Overview

Traditional password-based authentication systems are vulnerable to password theft, sharing, and brute-force attacks. This project demonstrates a biometric authentication approach by leveraging facial recognition technology to provide a more secure and user-friendly access mechanism.

The system captures and stores a registered face image, extracts facial features, and compares them against live webcam input in real time. Upon a successful match, access is granted instantly.

---

## ✨ Features

* 📷 Face Registration using Webcam
* 🔍 Real-Time Face Detection and Recognition
* 🔐 Biometric Authentication System
* ⚡ Fast Facial Feature Matching
* 🖥️ Live Webcam Verification
* 🚀 Lightweight and Easy to Deploy
* 🛡️ Adjustable Recognition Security Threshold
* 📊 AI-Based Face Encoding Comparison

---

## 🏗️ System Workflow

### Face Registration

1. Launch the registration module.
2. Capture the user's face through the webcam.
3. Save the face image as the authorized identity.

### Face Authentication

1. Start the unlock module.
2. Detect faces from the live webcam feed.
3. Extract facial encodings.
4. Compare with the registered face encoding.
5. Grant access when a match is found.

---

## 🛠️ Technologies Used

| Technology       | Purpose                              |
| ---------------- | ------------------------------------ |
| Python           | Core Programming Language            |
| OpenCV           | Webcam Access & Image Processing     |
| Face Recognition | Facial Feature Extraction & Matching |
| NumPy            | Numerical Operations                 |
| dlib             | Face Detection Backend               |

---

## 📂 Project Structure

```text
Face_Unlock_System/
│
├── face_set.py
├── face_unlock.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https:https://github.com/vijaydevverse/Face_Unlock_System
cd Face_Unlock_System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Step 1: Register Your Face

```bash
python face_set.py
```

Controls:

* Press **S** to save face
* Press **Q** to quit

This creates:

```text
Registered_Face.jpg
```

---

### Step 2: Unlock Using Face Recognition

```bash
python face_unlock.py
```

The system will:

* Open webcam
* Detect face
* Compare with registered user
* Display **UNLOCKED** upon successful authentication

---

## 🎯 Authentication Logic

The project uses facial encodings generated through the Face Recognition library.

```python
match = face_recognition.compare_faces(
    [known_encoding],
    face_encoding,
    tolerance=0.45
)
```

### Security Levels

| Tolerance | Security  |
| --------- | --------- |
| 0.60      | Low       |
| 0.50      | Medium    |
| 0.45      | High      |
| 0.40      | Very High |

Lower tolerance values increase authentication strictness.

---

## 📈 Future Enhancements

* Multi-User Authentication
* Face Database Storage
* Anti-Spoofing Detection
* Liveness Verification
* GUI Dashboard with CustomTkinter
* Login Activity Tracking
* Voice Feedback System
* Face Mask Recognition
* Windows Login Integration
* Cloud-Based Authentication

---

## 🔒 Security Considerations

This project is intended for educational and portfolio purposes. For production environments, additional measures such as:

* Liveness Detection
* Anti-Spoofing Protection
* Encrypted Face Data Storage
* Multi-Factor Authentication

should be implemented.

---

## 📷 Sample Output

```text
Show your face to unlock

Face Matched.
Access Granted!
```

```text
UNLOCKED
```

---

## 🤝 Contributions

Contributions, improvements, and feature suggestions are welcome.

Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 👨‍💻 Author

**Vijay Krishnan P.M.**

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub. It helps support the project and encourages future development.
