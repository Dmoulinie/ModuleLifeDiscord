from datetime import datetime
import time
class Chronometre:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.elapsed = 0

    def begin(self):
        self.start = datetime.now()

    def stop(self):
        self.end = datetime.now()
        self.elapsed = self.end - self.start
        return self.elapsed

    def pause(self):
        self.end = datetime.now()
        self.elapsed = self.end - self.start

    def resume(self):
        self.start = datetime.now()


    def reset(self):
        self.start = datetime.now()
        self.end = 0
        self.elapsed = 0

    def getElapsedTime(self):
        return self.elapsed

chrono = Chronometre()