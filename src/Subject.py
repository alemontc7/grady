class Subject:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.evaluation_items = []
    
    def get_name(self):
        return self.name
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def show_subject(self):
        json_evaluation_items = [item.show_evaluation_item() for item in self.evaluation_items]
        json_subject = {
            "name": self.name,
            "description":self.description,
            "evaluation_items": json_evaluation_items
        }
        return json_subject
