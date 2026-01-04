# Security Overview – Task 3

## 🔐 Encryption Method Used
This system uses **AES (Advanced Encryption Standard)** for encrypting files before storage.  
AES is a symmetric encryption algorithm widely adopted for securing sensitive data due to its speed and strong security guarantees.

---

## 🗝️ Key Management
- A secret encryption key is generated and stored locally
- The same key is used for both encryption and decryption
- The key is excluded from version control using `.gitignore`

⚠️ In real-world systems, keys should be stored securely using environment variables or dedicated key management services.

---

## 📂 File Protection
- Uploaded files are encrypted immediately
- Encrypted files are unreadable if accessed directly
- Decryption only occurs during authorized download

---

## 🧪 Integrity & Security Testing
- Encrypted files fail to open in Microsoft Word
- Decrypted files restore original content correctly
- Screenshots provided as visual proof

---

## 🔎 Security Limitations
- No user authentication implemented
- Local key storage only
- Intended strictly for demonstration purposes

---

## ✅ Conclusion
This project demonstrates foundational secure file handling using AES encryption and highlights the importance of protecting data at rest.
