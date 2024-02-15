from datetime import datetime


def log(func):
    def wrapped_function(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        duration = (end - start).seconds
        hours = duration // 3600
        minutes = duration // 60
        seconds = duration % 60

        print(f"time of play: {hours}:{minutes}:{seconds}")
        return result
    
    return wrapped_function