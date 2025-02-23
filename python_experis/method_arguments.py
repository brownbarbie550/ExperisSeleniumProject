def student_details(name="no name", age=18):
    """the method will print the student details"""
    print(f"name: {name}, age: {age}")

student_details("Moshe", 38)
student_details("Moshe")
student_details(age=22, name="Dani")

def student_details_grades(name, age, *grades):
    """the method will print the student details and the grades average the is unknown nuber of grades arguments"""
    print(f"name: {name}, age: {age}")
    print(grades)
    if len(grades)>0:
        print(f"average: {sum(grades)/len(grades)}")


#an example of a method with unknown number of arguments + names (**kwargs)
def person_details(name, age, *children_names, **additional_details):
    """the method gets a person details with unknown number
    of arguments of children names and unknown number of extra
    arguments (name and value)"""
    print(f"name: {name}, age: {age}")
    print(children_names)
    print(additional_details)

student_details_grades("Moshe", 20)
student_details_grades("Moshe", 20, 100, 95, 70)
student_details_grades("Moshe", 20, 100, 95, 70, 50, 98)

print("===============================================")
person_details("Dani", 40)
person_details("Dani", 40, "aaa", "bbb", phone="0534263475", email="abe@abc.com")
