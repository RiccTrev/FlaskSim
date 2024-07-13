import os

   class Config:
       SECRET_KEY = 'your-secret-key'
       UPLOAD_FOLDER = '/home/runner/app/uploads'
       RESULT_FOLDER = '/home/runner/app/results'
       ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

   # app/routes.py
   from flask import Blueprint, render_template, request, send_file, redirect, url_for, current_app
   from werkzeug.utils import secure_filename
   import os
   from datetime import datetime
   from .utils import allowed_file, process_file
   from .models import HistoryEntry

   main = Blueprint('main', __name__)

   history = []

   @main.route('/', methods=['GET', 'POST'])
   def upload_file():
       if request.method == 'POST':
           if 'file' not in request.files:
               return redirect(request.url)
           file = request.files['file']
           if file.filename == '':
               return redirect(request.url)
           if file and allowed_file(file.filename):
               filename = secure_filename(file.filename)
               file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
               file.save(file_path)
               return redirect(url_for('main.compute', filename=filename))
       return render_template('upload.html')

   @main.route('/compute/<filename>')
   def compute(filename):
       try:
           result_filename = process_file(filename)
           history.append(HistoryEntry(filename, 'Success'))
           return send_file(os.path.join(current_app.config['RESULT_FOLDER'], result_filename), as_attachment=True)
       except Exception as e:
           history.append(HistoryEntry(filename, 'Failed'))
           return f"Error: {str(e)}", 500

   @main.route('/history')
   def show_history():
       return render_template('history.html', history=history)