from flask import Flask, render_template, request
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)

# Load Public Key
def load_public_key(file_path):
    with open(file_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())
    return public_key

# Load Private Key
def load_private_key(file_path):
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())
    return private_key

# Encrypt data with Public Key
def encrypt_data(public_key, data):
    encrypted_data = public_key.encrypt(
        data.encode('utf-8'),  # Convert data to bytes
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data

# Decrypt data with Private Key
def decrypt_data(private_key, encrypted_data):
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data.decode('utf-8')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["data"]
        action = request.form["action"]
        
        private_key_path = "private_key.pem"  # Update with your private key path
        public_key_path = "public_key.pem"   # Update with your public key path

        public_key = load_public_key(public_key_path)
        private_key = load_private_key(private_key_path)

        if action == "Encrypt":
            encrypted_data = encrypt_data(public_key, data)
            result = encrypted_data.hex()  # Convert to hex string for display
        elif action == "Decrypt":
            encrypted_data = bytes.fromhex(data)  # Convert from hex string back to bytes
            decrypted_data = decrypt_data(private_key, encrypted_data)
            result = decrypted_data
        
        return render_template("index.html", result=result)

    return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)
