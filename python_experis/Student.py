#objects exercise 2

class Student:

    def __init__(self, id_num, name, grade):
        self.id_num = id_num
        self.name = name
        self.grade = grade

    def checkpass(self):
        return self.grade >= 70

    def updategrade(self, percent):
        new_grade = self.grade * percent / 100 + self.grade
        if new_grade > 100:
            self.grade = 100
        else:
            self.grade = new_grade

    def print_details(self):
        print(f"student name: {self.name} student id: {self.id_num} student grade {self.grade}")



i_d = int(input("enter your id number: "))
student_name = input("enter your name: ")
student_grade = int(input("enter your grade: "))

student1 = Student(i_d, student_name, student_grade)
student1.print_details()

if student1.checkpass():
    print("bravoooo")
else:
    print("study harder")

percent = int(input("enter a factor: "))
student1.updategrade(percent)
student1.print_details()


