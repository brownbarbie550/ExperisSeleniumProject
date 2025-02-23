#a method that gets 2 numbers(2 parameters/ 2 arguments) and returns the average
def average(a,b):
    if 1<=a<=100 and 1<=b<=100:
        avg = (a+b)/2
        return avg
    else:
        print("invalid numbers")

#get 2 grades from the user and print if the average grade is good or failed
grade1 = int(input("enter first grade: "))
grade2 = int(input("enter second grade: "))

avg = average(grade1, grade2)

if average(grade1, grade2) >= 70:
    print(f"{avg} bravoooo")
else:
    print(f"{avg}do better next time")

print(average(grade1, 100))
print(average(80,200))