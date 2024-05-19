# Secure File Storage System

## Introduction
This is a secure file storage system implemented using Flask for the web interface and cryptography for file encryption and decryption. Users can upload files, which are then encrypted before being stored on the server. Upon download, the files are decrypted and made available to the user.
```markdown
## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd secure_file_storage
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the secret key:
   Replace the placeholder `rIy6DXBU5MqJj6HrKix2MuzkG25SXNfjBsGwSvFZw0Y=` in `app.py` with your actual secret key.

## Usage
1. Run the application:
   ```bash
   python app.py
   ```

2. Access the application in your web browser at `https://localhost:5000`.

3. Register or log in to start uploading and downloading files securely.

## Features
- Secure file upload and download
- User authentication and session management
- Encrypted file storage on the server
- Flash messages for feedback

## Dependencies
- Flask: 2.0.2
- cryptography: 36.0.0

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
