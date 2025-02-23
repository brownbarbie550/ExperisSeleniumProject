from StudentC import StudentC


class CourseC:
    #attributes: course_number, course_name, subjects and lecturer name list
    #list of students, max students in class

    def __init__(self, cour_num, cour_name, max_stud):
        self.cour_num = cour_num
        self.cour_name = cour_name
        self.max_stud = max_stud
        self.sub_lect_dict = {}
        self.stud_list = []

    def __str__(self):
        return (f"course number: {self.cour_num}, course name: {self.cour_name}, max students: {self.max_stud},"
                f" sub and lecturer: {self.sub_lect_dict}, students list: {self.stud_list} ")

    def add_student(self, student: StudentC):
        if len(self.stud_list) == self.max_stud:
            print("the course is full")
            return False
        self.stud_list.append(student)

    def add_factor(self, subject, percent):
        for student in self.stud_list:
            student.calc_factor(subject, percent)

    def del_student(self, student: StudentC):
        self.stud_list.remove(student)

    def averages(self):
        averages = {}
        for stud in self.stud_list:
            averages[stud.id_num] = stud.averages()
        if self.stud_list == []:
            return None
        return averages


    def weak_students(self):
        averages = self.averages()
        min_avg = min(averages.values())
        lowest_avg = []
        for id_num in averages:
            if averages[id_num] == min_avg:
                lowest_avg.append(id_num)
        return lowest_avg


if __name__ == "__main__":
    course1 = CourseC(1, "qa", 10)
    print(course1)
    student1 = StudentC(123456789, 25, "dagmawit")
    student2 = StudentC(987654321, 24, "dagi")
    student3 = StudentC(123654789, 20, "dagisha")
    student4 = StudentC(789456123, 26, "dagim")

    student1.add_grade("maths", 70)
    student1.add_grade("QA", 80)

    student2.add_grade("english", 100)
    student2.add_grade("maths", 94)

    student3.add_grade("history", 70)
    student3.add_grade("QA", 80)

    student4.add_grade("maths", 90)
    student4.add_grade("english", 78)
    print(course1.averages())
    print(course1.weak_students())


# if __name__ == "__main__":
#     course1 = CourseC("course number1", "cyber course", 40)
#
#     while True:
#         topic_name = input("enter topic name or 'done': ")
#         if topic_name.lower() == "done":
#             break
#         lecturer_name = input(f"enter lecturer name for {topic_name}")
#     student.sub_lect_dict[topic_name] = lecturer_name
#
#     for i in range(student.id_num):
#         if student.id_num != 0 and len(student.stud_list) != student.max_stud:
#             details= student.stud_name(student) and student.grades
#             print(details)
#             for student in student.stud_name:
#                 student.grades(details)




























