import os
import random
from flask import current_app

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def process_file(filename):
    # Randomly return 1 or 0
    result = random.choice([0, 1])
    result = 1
    if result == 0:
        raise ValueError("Random processing error occurred")
    
    # This is where you would call your Python script to process the file
    # For now, we'll just simulate a computation
    result_filename = f"result_{filename}"
    result_path = os.path.join(current_app.config['RESULT_FOLDER'], result_filename)
    
    # Ensure the result directory exists
    if not os.path.exists(current_app.config['RESULT_FOLDER']):
        os.makedirs(current_app.config['RESULT_FOLDER'])
    
    # Simulate processing (replace this with your actual script)
    result_content = "Computation result"
    with open(result_path, 'w') as f:
        f.write(result_content)
    
    return result_filename, result_content
