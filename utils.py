from datetime import datetime
import os

def get_datatime_str():
    return datetime.now().strftime("%m-%d-%Y-%H-%M-%S")

def split_filename(filename):
    return os.path.splitext(filename)
