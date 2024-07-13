import os
   from flask import current_app

   def allowed_file(filename):
       return '.' in filename and \
              filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

   def process_file(filename):
       # This is where you would call your Python script to process the file
       # For now, we'll just simulate a computation
       result_filename = f"result_{filename}"
       result_path = os.path.join(current_app.config['RESULT_FOLDER'], result_filename)
       
       # Simulate processing (replace this with your actual script)
       with open(result_path, 'w') as f:
           f.write("Computation result")
       
       return result_filename