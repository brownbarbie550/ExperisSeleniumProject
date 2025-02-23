#objects exercise 1

class Course:

    def __init__(self, course_num, course_name, students_course, max_students):
        self.course_num = course_num
        self.course_name = course_name
        self.students_course = students_course
        self.max_students = max_students

    def free_spots(self):
        return self.max_students - self.students_course

    def new_studs(self, new_stud):
        available = self.free_spots()
        if new_stud <= available:
            self.students_course += new_stud
        else:
            self.students_course += available

    def __str__(self):
        return (f"course number: {self.course_num}\n"
                f"course name: {self.course_name}\n"
                f"students enrolled: {self.students_course}\n"
                f"max students: {self.max_students}")





course_number =int(input("enter course number: "))
course_name = input("enter course name: ")
students_enrolled = int(input("enter number of students enrolled: "))
max_students = int(input("enter max number of students: "))

course = Course(course_number, course_name, students_enrolled, max_students)

print("Course details before registration: ")

new_stud = int(input("enter number of new students to register: "))

course.new_studs(new_stud)

print("course details after registration: ")
print(course)





