from datetime import datetime

    class HistoryEntry:
        def __init__(self, filename, status):
           self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           self.filename = filename
           self.status = status