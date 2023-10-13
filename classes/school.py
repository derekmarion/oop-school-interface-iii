from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.staff = Staff.load_staff()
        self.students = Student.load_students()

    @property
    def get_students(self):
        i = 1
        print("\n---ALL STUDENTS---")
        for student in self.students:
            print(f"{i}. {student['name']} {student['school_id']}")
            i += 1

    def get_student_by_id(self, school_id):
        for student in self.students:
            if student['school_id'] == school_id:
                return f"\n{student['name'].upper()}\n------------\nAge: {student['age']}\nID: {student['school_id']}"
    
    def add_student(self, student_data):
        self.students.append(student_data)

    def delete_student(self,school_id):
        for student in self.students:
            if student['school_id'] == school_id:
                self.students.remove(student)