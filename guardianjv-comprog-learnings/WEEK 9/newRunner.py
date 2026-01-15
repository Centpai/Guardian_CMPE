class Student:

    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info(self):
        print(f"{self.name} grade:{self.grade} subject:{self.subject}")


if __name__ == "__main__":

    student1 = Student(name="Vincent", grade=1.25, subject=["Physics", "Chemistry"])
    student1.print_student_info()

    student2 = Student(name="Vincent", grade=1.00, subject=["Physics", "Chemistry"])
    student2.print_student_info()

    student3 = Student(name="Vincent", grade=1.75, subject=["Physics", "Chemistry"])
    student3.print_student_info()
