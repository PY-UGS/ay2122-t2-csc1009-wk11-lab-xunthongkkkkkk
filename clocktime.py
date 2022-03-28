from datetime import time
class clockTime:
    def __init__(self):
        self.hours = input("Enter hours: ")
        self.mins = input("Enter minutes: ")
        self.seconds = input("Enter seconds: ")

    def setHours(self, hrs):
        self.hours = hrs
        
    def setMinutes(self, mins):
        self.mins = mins

    def setSeconds(self, secs):
        self.seconds = secs

    def setTime(self, hours, mins, secs):
        self.setHours(hours)
        self.setMinutes(mins)
        self.setSeconds(secs)

    def showTime(self):
        t = time(int(self.hours), int(self.mins), int(self.seconds))
        return t

clocktime = clockTime()
print(clocktime.showTime())
    