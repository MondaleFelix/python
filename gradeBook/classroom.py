class Classroom():
    assignment = None

    def __init__(self, class_name,):
        self.class_name = class_name
        self.class_dates = ()
        self.roster = {}
        self.student_assignments = []
        self.student_grades = {}

        # This function add assignments
    def add_assignment(self, assignment):
        if assignment in self.student_assignments:
            print("Assignment already inputted")
        else:
            self.student_assignments.append(assignment)

        # This function deletes specified assignment
    def delete_assignment(self, assignment):
        if assignment in self.student_assignments:
            self.student_assignments.remove(assignment)
        else:
            print("Assignment not found")
