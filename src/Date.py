class Date:
    def __init__(self, day, month, year, hour, minutes, seconds):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
    
    def get_date(self):
        date = self.day + "/" + self.month + "/" + self.year
        return date
    
    def show_date(self):
        json_date = {
            "day": self.day,
            "month": self.month,
            "year": self.year,
            "hour": self.hour,
            "hour": self.minutes,
            "hour": self.seconds,
        }
        return json_date