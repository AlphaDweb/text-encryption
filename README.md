# Asymmetric Encryption and Decryption Web Application
This repository implements a Flask-based Web Application for encrypting and decrypting data using RSA Asymmetric Encryption. It allows users to securely encrypt data with a public key and decrypt it using a private key.

# Features
Asymmetric Encryption (RSA):

Encrypts plaintext data using a public key.
Decrypts encrypted data using a private key.
Secure Key Management:

Loads PEM-encoded RSA keys for encryption and decryption.
Uses secure padding (OAEP) with SHA-256 hashing.
Web-Based Interface:

Built with Flask for user-friendly encryption and decryption operations.
Accepts user input through HTML forms.

# Applications
Secure Messaging: Ensures private and confidential communication.
Data Protection: Encrypts sensitive information before storage or transmission.
Authentication Systems: Verifies user identity through encrypted data exchange.
Technical Stack
Flask: Lightweight web framework for creating the application.
Cryptography Library: Provides secure encryption and decryption using RSA.
Python 3: Programming language used for implementation.

# Installation
```bash 
https://github.com/AlphaDweb/text-encryption.git
cd rsa-encryption-webapp
```
### 2. Install Dependencies:
```bash 
pip install -r requirements.txt
```
**Note:** Create a `requirements.txt` file with the following content:

### 3. Generate RSA Keys:
Run the following commands to generate a private key and public key:

# Generate Private Key
openssl genrsa -out private_key.pem 2048  

# Extract Public Key
openssl rsa -in private_key.pem -pubout -out public_key.pem  
Usage
Run the Flask Application:
bash
Copy code
python app.py
Access the Web Interface:
Open your browser and go to:

`http://127.0.0.1:5000`

# Encrypt Data:

Enter plaintext data and select the Encrypt option.
Copy the encrypted output (in hexadecimal format).
Decrypt Data:
Paste the encrypted data and select the Decrypt option.
View the original plaintext output.
Project Structure
```
rsa-encryption-webapp/
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html         # Web interface template
├── private_key.pem        # Private key (generated separately)
├── public_key.pem         # Public key (generated separately)
├── requirements.txt       # Dependencies
```
## Contributing
Contributions are welcome!

Feel free to fork this repository and improve the project.
Submit a pull request if you have enhancements or bug fixes.

## Acknowledgments
Flask for providing a lightweight web framework.
Cryptography library for secure encryption algorithms.
OpenSSL for generating RSA keys.
Special thanks to the open-source community for their support and resources.
