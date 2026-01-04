# Secure File Sharing System (AES Encryption)

## 📌 Project Overview
This project is a secure file sharing web application built with **Python Flask** that allows users to upload and download files safely.  
All uploaded files are encrypted using **AES (Advanced Encryption Standard)** before being stored and decrypted only when downloaded.

The system simulates real-world secure data handling used in industries such as legal, healthcare, and corporate environments.

---

## 🚀 Features
- Secure file upload and download
- AES encryption for files at rest
- Automatic decryption on file download
- Simple and user-friendly web interface
- Basic encryption key management
- Demonstration of encrypted vs decrypted files

---

## 🛠️ Technologies Used
- **Python**
- **Flask**
- **PyCryptodome (AES Encryption)**
- **HTML / CSS**
- **Git & GitHub**

---

## ⚙️ How It Works
1. User uploads a file through the web interface
2. File is encrypted using AES before storage
3. Encrypted file is saved on the server
4. When downloading, the file is decrypted and returned to the user
5. Encrypted files remain unreadable outside the system

---

## 🧪 Proof of Security
Screenshots included in the `screenshots/` folder show:
- Encrypted file unreadable in Microsoft Word
- Decrypted file restored correctly after download
- Flask server running
- Successful file upload via browser

---
FUTURE_CS_03/
│── app.py
│── uploads/               # Temporarily stores uploaded files
│── encrypted_files/       # Stores AES-encrypted files
│── screenshots/           # Proof of working system
│── docs/
│   └── security_overview.md
│── README.md
│── .gitignore


## ▶️ How to Run
```bash
python app.py

http://127.0.0.1:5000

👤 Author

Ngwoke Makuochukwu Mark
Cybersecurity intern at Future Intern

