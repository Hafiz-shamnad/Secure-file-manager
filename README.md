# **Secure File Storage System**

## **Introduction**
Secure File Storage System is a web application built using Flask and cryptography, allowing users to securely upload, store, and download files. The system encrypts files before storing them on the server and decrypts them upon retrieval, ensuring data security and confidentiality.

## **Installation**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hafiz-shamnad/Secure-file-manager.git
   cd secure_file_storage
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the secret key:**
   Replace the placeholder 'your_secret_key` in `app.py` with your actual secret key.

## **Usage**
1. **Run the application:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your web browser and go to `https://localhost:5000`.

3. **Register or log in:**
   Create a new account or log in with your existing credentials to start using the application.

4. **Upload files securely:**
   Choose a file, upload it, and it will be securely encrypted before storage.

5. **Download files securely:**
   Access your uploaded files and download them securely. They will be decrypted upon download.

## **Features**
- Secure file upload and download
- User authentication and session management
- Encrypted file storage on the server
- Flash messages for feedback

## **Dependencies**
- Flask: 2.0.2
- cryptography: 36.0.0

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.
