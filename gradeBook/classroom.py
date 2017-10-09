class Classroom():

    def __init__(self, class_name,):
        self.class_name = class_name
        self.class_dates = ()
        self.roster = {}
        self.student_assignments = []
        self.student_grades = {}

    def add_assignment(self, assignment):
        assignment = None
        self.student_assignments.append(assignment)
        print("Added {} to student assignments".format(assignment))



class Student():

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
