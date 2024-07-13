from . import db
from datetime import datetime

class ScriptInvocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    filename = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    result = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<ScriptInvocation {self.filename} {self.status}>'