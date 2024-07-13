import os

class Config:
    SECRET_KEY = 'your-secret-key'
    UPLOAD_FOLDER = '/path/to/uploads'
    RESULT_FOLDER = '/path/to/results'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
