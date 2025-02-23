#objects exercise 3

class Person:
    def __init__(self, name, age, num_children):
        self.name = name
        self.age = age
        self.num_children = num_children

    def got_kids(self):
        return self.num_children > 0

    def age_group(self):
        if 0 < self.age <= 18:
            return "child"
        elif 19 <= self.age <= 60:
            return "adult"
        elif 61 <= self.age <= 120:
            return "senior"

    def print_details(self):
        print(f"name: {self.name} age{self.age} number of kids{self.num_children}")




new_name = input("enter your name: ")
new_age = int(input("enter your age: "))
num_kids = int(input("enter your number of kids: "))

personal_info = Person(new_name, new_age, num_kids)
personal_info.print_details()

if personal_info.got_kids():
    print(f"it is such a blessing")
else:
    print(f"you dont have children")

print(personal_info.age_group())



