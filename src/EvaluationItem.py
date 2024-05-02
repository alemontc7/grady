from Date import Date

class EvaluationItem:
    def __init__(self, description, grade, date):
        self.description = description
        self.grade = grade
        if not isinstance(date, Date):
            raise ValueError("Date must be an instance of the Date class")
        self.date = date
    
    def get_grade(self):
        return self.grade
    
    def get_date(self):
        return self.date

    def get_description(self):
        return self.description

    def show_evaluation_item(self):
        json_show_evaluation_item = {
            "description": self.description,
            "grade": self.grade,
            "date": self.date.show_date()
        }
        return json_show_evaluation_item
        

