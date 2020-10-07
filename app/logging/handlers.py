import pathlib
from logging import handlers
import os


def mkdir(directory):
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)


class MakeDirTimedRotatingFileHandler(handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None):
        mkdir(os.path.dirname(filename))
        handlers.TimedRotatingFileHandler.__init__(self, filename, when, interval, backupCount, encoding, delay, utc, atTime)
