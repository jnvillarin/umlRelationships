#Association
class Student:
    def __init__(self, name):
        self.name = name
 
 
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
 
    def add_student(self, student):
        self.students.append(student)
 
    def show_students(self):
        print(f"{self.name} teaches:")
        for s in self.students:
            print(f" - {s.name}")
 
 
alice = Student("Alice")
bob = Student("Bob")
teacher = Teacher("Mr. Smith")
teacher.add_student(alice)
teacher.add_student(bob)
teacher.show_students()
