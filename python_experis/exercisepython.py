# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = num1+num2
# if num3 % 2 == 0:
#     print("valid number")

# num1 = int(input("enter a number: "))
# if 100 <= num1 <= 999:
#     a = num1 % 10
#     b = num1 % 100 // 10
#     c = num1 // 100
#     sum1 = a + b + c
#     print(sum1)


# a = num3 % 10           # right digit
# b = num3 % 100 // 10    # middle digit
# # b = num3 // 10 % 10
# c = num3 // 100         # left digit (for a 3 digits number)
# print(c)
# print(b)
# print(a)

# age = int(input("enter your age: "))
# if age <= 18:
#     print("child")
# elif age == 19 and age >= 60:
#     print("adult")
# else:
#     print("senior")


# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# if num1 % 2 == 0 and num2 % 2 == 0:
#     sumadd = num1 + num2
#     print(sumadd)
# else:
#     multi = num1 * num2
#     print(multi)

# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# addition = num1 + num2
# if addition == 10:
#     print("yes")

# grade = int(input("enter your grade: "))
# while 0 > grade <= 100:
#     if grade >= 100:
#         print("bravo")
#     elif grade < 70:
#         print("study more")
# else:
#     print("invalid grade")
#
# num = int(input("enter a number: "))
# if 10 >= num <= 99:
#     if num % 7 == 0:
#         print("lucky number")

# day = int(input("Enter day (1-31): "))
# month = int(input("Enter month (1-12): "))
# year = int(input("Enter year (1950-2020): "))
# if 1 <= day <= 31 and 1 <= month <= 12 and 1950 <= year <= 2020:
#     formatted_year = str(year % 100).zfill(2)
#     print(f"{day}/{month}/{formatted_year}")
# else:
#     print("Error: One or more values entered are invalid.")





# from random import randint
# list1 = []
# for i in range(10):
#     ranums = randint(1,100)
#     list1.append(ranums)
# print(list1)

list_one = [1,2,3,4,5,6,7,8,9,10]
# listn = []
# listn.append(list_one[7:])
# print(listn)

# print(list_one[::-1])
# print(list_one[::2])

# lislist = []
# lislist.append(list_one[:5])
# print(lislist)

# listt = []
# listt.append(list_one[::2])
# print(listt)

# num = int(input("enter a number: "))
# newlist = list_one[:7] + [num] + list_one[10:]
# print(newlist)

# relist = []
# for num in list_one:
#     if num % 3 == 0:
#         list_one.remove(num)
#         relist.append(num)
# print(relist)
# print(list_one)
#
# new_list = [1,1,2,3,5,8,13,21,34]

input_string = input("Enter a string: ")
unique_chars = []
for char in input_string:
    if char not in unique_chars:
        unique_chars.append(char)
print("List of unique characters:", unique_chars)





















