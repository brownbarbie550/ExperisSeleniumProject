#exercise1
# def sum_of_nums(num):
#     hundreds = num // 100
#     tens = (num // 10) % 10
#     ones = num % 10
#     return hundreds + tens + ones
#
# num = int(input("enter a 3-digit number: "))
# if 100 <= num <= 999:
#     result = sum_of_nums(num)
#     print("the sum of the digits is:", result)
# else:
#     print("the numbers must be between 100 and 999")



#exercise2
# def legal_num(user):
#     if 100 <= user <= 999:
#         print("this number is legit")
#     else:
#         print("enter a 3 digit number that is legit")
# user = int(input("enter a number: "))
# legal_num(user)



#exercise3
# def num_str(number, string):
#     for i in range(number):
#         print(string)
# number = int(input("enter a number: "))
# string = input("type in something: ")
#
# num_str(number, string)



#exercise4
# def sum_nums(num):
#     summ = 0
#     for i in range(1, num + 1):
#         summ += i
#     return summ
# user = int(input("enter a number: "))
# result = sum_nums(user)
# print(f"the sum of the numbers from 1 to {user} is: {result}")



#exercise5
# def sum_of_nums(num):
#     sumsum = 0
#     for i in range(1, num + 1):
#         sumsum += i
#     return sumsum
# for j in range(5):
#     user = int(input("enter a number: "))
#     result = sum_of_nums(user)
#     print(f"the sum of the numbers from 1 to {user} is: {result}")



#exercise6
# def two_nums(num1, num2):
#     for i in range(num1, num2 + 1):
#         print(i, end=" ")
#     print()
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# two_nums(num1, num2)



#exercise7
# def two_nums(num1, num2):
#     result = 1
#     for i in range(num1):
#         result *= num2
#     return result
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# result = two_nums(num1, num2)
# print(f"{num1} raised to the power of {num2} is : {result}")



#exercise8
# def categories(age):
#     if age <= 18:
#         print("child")
#     elif age <= 60:
#         print("adult")
#     else:
#         print("senior")
# for i in range(5):
#     age = int(input("enter your age: "))
#     categories(age)



#exercise9
# def grades(grade):
#     if grade >= 70 and grade <= 100:
#         print("bravoooo")
#     else:
#         print("study harder")
# for i in range(5):
#     grade = int(input("enter your grade: "))
#     grades(grade)



#exersice10
# list_one = []
# def numbers():
#     for i in range(2, 40):
#         if i % 2 == 0:
#             list_one.append(i)
# numbers()
# print(list_one)



#exercise11
# list1 = []
# from random import randint
# def numbers():
#     for i in range(20):
#         rand_nums = randint(1,100)
#         list1.append(rand_nums)
# numbers()
# print(list1)
# user = int(input("enter a number: "))
# for j in range(user):
#     print(list1)




#exercise12
# list1 = []
# from random import randint
# def numbers():
#     for i in range(20):
#         rand_nums = randint(1,100)
#         list1.append(rand_nums)
# numbers()
# print(list1)
# user = int(input("enter a number: "))
# for j in range(user):
#     print(list1)
#
# def find_max_index(lst):
#     max_value = max(lst)
#     return lst.index(max_value)
# max_index = find_max_index(list1)
# print(f"the index of the maximum value is: {max_index}")




#exercise13
# def get_grades(student):
#     grade_list = []
#     for i in range(student):
#         grade = int(input(f"enter a grade for student {i+1}: "))
#         grade_list.append(grade)
#     return grade_list
#
# num_students = int(input("enter the number of students: "))
# grade_list = get_grades(num_students)
# print("the grades of the students are:", grade_list)





#exercise14
# def get_grades(student):
#     grade_list = []
#     for i in range(student):
#         grade = int(input(f"enter a grade for student {i+1}: "))
#         grade_list.append(grade)
#     return grade_list
#
# def calc_avg(grade_list):
#     total = sum(grade_list)
#     avg = total / len(grade_list)
#     return avg
#
# num_students = int(input("enter the number of students: "))
# grade_list = get_grades(num_students)
# avg = calc_avg(grade_list)
# print("the grades of the students are:", grade_list)
# print(f"the average grade is: {avg:.2f}")