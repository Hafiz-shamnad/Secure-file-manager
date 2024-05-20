from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet, InvalidToken
import os
import tempfile ,shutil


app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

# Path to the uploads directory
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Replace 'your_secret_key_here' with your actual secret key
SECRET_KEY = "Your_Seceret_Key" 
cipher = Fernet(SECRET_KEY)

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_data = file.read()
            encrypted_data = cipher.encrypt(file_data)
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb') as f:
                f.write(encrypted_data)
            return render_template('upload.html', success=True)
    return render_template('upload.html', success=False)




@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        decrypted_data = cipher.decrypt(encrypted_data)
        
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(decrypted_data)
        temp_file.close()
        
        destination_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        shutil.move(temp_file.name, destination_path)
        
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except InvalidToken:
        flash('Error: Unable to decrypt the file. Please try again or contact support.', 'danger')
    except Exception as e:
        flash(f'Error: {e}', 'danger')
    
    return redirect(url_for('index'))


@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if os.path.exists(file_path):
        os.remove(file_path)
        flash(f'File "{filename}" deleted successfully!', 'success')
    else:
        flash(f'File "{filename}" not found!', 'danger')
    
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Add authentication logic here
        session['username'] = username
        return redirect(url_for('index'))
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
