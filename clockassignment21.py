class Time:
    def __init__(self, hour=0, min=0):
        self.hour = hour
        self.min = min

    def Tick(self):
        self.min += 1
        if self.min ==60:
            self.min = 0
            self.hour = (self.hour + 1) % 24

    def __sub__(self, other):
        diff_hour = self.hour - other.hour
        diff_min = self.min - other. min
        if diff_min < 0:
            diff_min += 60
            diff_hour -= 1
        return diff_hour, diff_min
    def __str__(self):
        return  f"{self.hour}:{self.min}"
    def getTime(self):
        return self.hour, self.min
    def setTime(self, hour, min):
        self.hour = hour
        self.min = min
    def __It__(self, other):
        return(self.hour, self.min) < (other.hour, other.min)
    def __len__(self):
        return self.hour * 60 + self.min

