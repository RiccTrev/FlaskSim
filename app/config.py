import os

class Config:
    SECRET_KEY = 'your-secret-key'
    UPLOAD_FOLDER = os.path.join(os.path.expanduser('~'), 'FlaskSim', 'uploads')
    RESULT_FOLDER = os.path.join(os.path.expanduser('~'), 'FlaskSim', 'results')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
