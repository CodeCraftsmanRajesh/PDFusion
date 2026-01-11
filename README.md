# 📄 PDFusion — Merge & Split PDFs Securely

A modern, privacy-focused web application built with Flask that allows users to merge multiple PDF files and split PDFs by selecting custom page numbers, featuring a beautiful UI, dark mode, drag-and-drop uploads, and instant downloads without storing user files on the server.


## 🚀 Live Demo

<link href="https://pdfusion-o6kj.onrender.com/">Click here</link>

## ✨ Features

- 📎 Merge unlimited PDF files
- ✂️ Split PDFs by selecting specific (random) page numbers
- 🔍 Page preview before splitting
- 🧾 Page count validation UI
- 🧲 Drag & drop file upload with smooth animations
- 🌙 Light / Dark mode toggle
-⚡ Instant download (no server-side file storage)
- 🔐 Privacy-first: PDFs processed entirely in memory
- 📱 Responsive & modern UI
- 🚀 Deployment-ready configuration

## 🔐 Privacy & Security (Important)

- ❌ No uploaded files are stored on disk
- ❌ No database is used
- ✅ All PDFs are processed in memory using streams
- ✅ Files are discarded immediately after download

This approach ensures maximum user privacy and eliminates the need for persistent storage.

## 🛠️ Tech Stack
### Backend
- Flask (Python)
- PyPDF2 — PDF merging & splitting
- Gunicorn — Production WSGI server

### Frontend
- HTML5 / CSS3
- Bootstrap
- Animate.css
- Google Fonts (Poppins)

## Deployment

Render

GitHub

### 📂 Project Structure
```bash
PDFusion/
│
├── app.py
├── requirements.txt
├── render.yaml
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── logo.png
│
└── templates/
    ├── base.html
    ├── index.html      # Merge PDFs
    └── split.html      # Split PDFs
```
## ⚙️ Local Setup
###1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/pdf-toolkit.git
cd pdf-toolkit
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
python app.py
```
---
## 🧠 Learning Outcomes

- Flask routing & file handling
- In-memory PDF processing using Python streams
- Secure file uploads without storage
- Modern UI/UX design (dark mode & animations)
- Cloud deployment best practices
---
## 📌 Future Enhancements

- 📐 Page thumbnail previews
- 📦 ZIP download for split PDFs
- ♿ Accessibility improvements
- 🌐 Multi-language support

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Rajesh
Computer Science Student
