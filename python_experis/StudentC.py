class StudentC:
    #attributes: id_num, age, list of subjects and grades, where every subject got grade

    def __init__(self, id_num, age, stud_name):
        if type(id_num) != int:
            raise TypeError("invalid input enter numbers")
        if type(age) != int:
            raise TypeError("invalid input enter numbers")
        if age < 6:
            raise TypeError("invalid age you have to be older than 6")
        if type(stud_name) != str:
            raise TypeError("invalid input")
        self.id_num = id_num
        self.age = age
        self.stud_name = stud_name
        self.grades = {}


    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def __str__(self):
        return f"stud_id: {self.id_num} \n stud_age: {self.age} \n list of every subject and it's grade {self.grades}"

    def calc_factor(self, percent, subject):
        new_grade = self.grades[subject] + self.grades[subject] * percent / 100
        if new_grade > 100:
            self.grades[subject] = 100
        else:
            self.grades[subject] = new_grade


    def average(self):
        grades_avg = sum(self.grades.values()) / len(self.grades)
        return grades_avg

    def __eq__(self, other):
        return self.id_num == other.id_num

    def __gt__(self, other):
        return self.age > other.age



if __name__ == "__main__":
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
    print(student1)
    print(student2)

    student1.calc_factor(10, "maths")
    print(student1)

    student2.calc_factor(10, "maths")
    print(student2)

    print(student1.average())
    print(student2.average())
    print(student3.average())
    print(student4.average())














