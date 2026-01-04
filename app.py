from flask import Flask, request, send_file, render_template_string
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted_files"
KEY_FILE = "secret.key"

# Generate or load AES key
if not os.path.exists(KEY_FILE):
    key = get_random_bytes(32)  # AES-256
    with open(KEY_FILE, "wb") as f:
        f.write(key)
else:
    with open(KEY_FILE, "rb") as f:
        key = f.read()

def encrypt_file(filepath, output_path):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(filepath, "rb") as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(output_path, "wb") as f:
        f.write(cipher.nonce + tag + ciphertext)

def decrypt_file(filepath, output_path):
    with open(filepath, "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    with open(output_path, "wb") as f:
        f.write(data)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        upload_path = os.path.join(UPLOAD_FOLDER, file.filename)
        encrypted_path = os.path.join(ENCRYPTED_FOLDER, file.filename + ".enc")

        file.save(upload_path)
        encrypt_file(upload_path, encrypted_path)

        return "File uploaded and encrypted successfully!"

    return render_template_string("""
        <h2>Secure File Upload (AES Encryption)</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <button type="submit">Upload</button>
        </form>
        <br>
        <a href="/download">Download decrypted file</a>
    """)

@app.route("/download")
def download():
    encrypted_files = os.listdir(ENCRYPTED_FOLDER)
    if not encrypted_files:
        return "No encrypted files available."

    enc_file = encrypted_files[0]
    enc_path = os.path.join(ENCRYPTED_FOLDER, enc_file)
    output_path = "decrypted_" + enc_file.replace(".enc", "")

    decrypt_file(enc_path, output_path)
    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
