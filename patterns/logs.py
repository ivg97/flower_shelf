import datetime

class Log:
    auto_id = 1
    def __init__(self, name, date=datetime.datetime.now().strftime('%d %B %Y'), time=datetime.datetime.now().strftime('%H:%M:%S')):
        self.id = Log.auto_id
        Log.auto_id += 1
        self.date = date
        self.time = time
        self.name = name

