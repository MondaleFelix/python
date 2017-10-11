class Student():

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignment = {}

    def get_gpa(self):
        final = 0
        for i in self.assignment.values():
            final += i
        return final / len(self.assignment)

    def add_assignment(self, assignment, grade):
        self.assignment[assignment] = grade


    def delete_assignment(self, assignment):
        self.assignment.pop(assignment)


    def update_assignment(self, assignment, grade):
        delete_assignment(assignment)
        add_assignment(assignment, grade)
        #DRY

    def get_assignment(self):
        return self.assignment
