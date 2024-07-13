from flask import Blueprint, render_template, request, redirect, url_for, current_app
from werkzeug.utils import secure_filename
import os
from .utils import allowed_file, process_file
from .models import ScriptInvocation
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def upload_file():
    message = None
    message_class = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            message = "No file part"
            message_class = "danger"
            return render_template('upload.html', message=message, message_class=message_class)
        
        file = request.files['file']
        if file.filename == '':
            message = "No selected file"
            message_class = "danger"
            return render_template('upload.html', message=message, message_class=message_class)
        
        if not allowed_file(file.filename):
            message = "File extension not allowed"
            message_class = "danger"
            return render_template('upload.html', message=message, message_class=message_class)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            file_path = os.path.join(upload_folder, filename)
            
            # Ensure the upload directory exists
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder, exist_ok=True)

            file.save(file_path)
            
            try:
                result_filename, result_content = process_file(filename)
                invocation = ScriptInvocation(filename=filename, status='Success', result=result_content)
                db.session.add(invocation)
                db.session.commit()
                message = f"File {filename} successfully processed."
                message_class = "success"
            except Exception as e:
                invocation = ScriptInvocation(filename=filename, status='Failed', result=str(e))
                db.session.add(invocation)
                db.session.commit()
                message = f"Error processing file {filename}: {str(e)}"
                message_class = "danger"
    
    return render_template('upload.html', message=message, message_class=message_class)

@main.route('/compute/<filename>')
def compute(filename):
    try:
        result_filename, result_content = process_file(filename)
        invocation = ScriptInvocation(filename=filename, status='Success', result=result_content)
        db.session.add(invocation)
        db.session.commit()
        return render_template('upload.html', message=f"File {filename} successfully processed.", message_class="success")
    except Exception as e:
        invocation = ScriptInvocation(filename=filename, status='Failed', result=str(e))
        db.session.add(invocation)
        db.session.commit()
        return render_template('upload.html', message=f"Error processing file {filename}: {str(e)}", message_class="danger")

@main.route('/history')
def show_history():
    invocations = ScriptInvocation.query.order_by(ScriptInvocation.timestamp.desc()).all()
    return render_template('history.html', invocations=invocations)
