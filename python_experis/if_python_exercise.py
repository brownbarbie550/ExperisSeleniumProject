
# exercise 1
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# result = num1 + num2
# # print(result)
# if result % 2 == 1:
#     print("the result is odd")
# else:
#     print("the result is even")


# exercise 2
# number = int(input("Please enter a number: "))
# if number in range(100,999):
#     num1 = number % 10
#     num2 = number // 10 % 10
#     num3 = number // 100 % 10
#     result = num1 + num2 + num3
#     print(result)
# else:
#     print("error")



#exercise 3
# age = int(input("how old are you?: "))
# if age in range(0,18):
#     print("child")
# elif age in range(19,60):
#     print("adult")
# elif age in range(61,120):
#     print("senior")
# else:
#     print("error")



#exercise 4
# num1 = int(input("give me a number: "))
# num2 = int(input("give me another number: "))
# if num1 % 2 == 0 and num2 % 2 == 0:
#     num3 = num1 + num2
#     print(num3)
# else:
#     num3 = num1 * num2
#     print(num3)


#exercise 5
# num1 = int(input("enter your favorite number: "))
# num2 = int(input("enter your second favorite number: "))
# if num1 + num2 == 10:
#     print("number equals to 10")
# else:
#     print("not equal to 10")



#exercise 6
# grade = int(input("enter your grade: "))
# if grade <= 100 and grade >= 70:
#     print("Brilliant!!!!")
# elif grade <= 100 and grade <= 70:
#     print("its okay you can improve next time:)")
# elif grade > 100:
#     print("ERROR!!!!!")



#exercise 7
# num = int(input("Please enter a number: "))
# if 10 <= num <= 99:
#     if '7' in str(num) or num % 7 == 0:
#         print("Lucky number")
#     else:
#         print("Not a lucky number")
# else:
#     print("Error: The number is not two-digit")
#anothe way to solve it
# a= num % 10
# b = num // 10
# if a == 7 or b == 7 or num % == 0:
#     print("lucky number")
# else:
#     print("not a lucky number")


# exercise 8
# day = int(input("Please enter a day: "))
# month = int(input("Please enter a month: "))
# year = int(input("Please enter a year: "))
#
# if year < 1950 or year > 2020:
#     print("Error: Invalid year")
# else:
#     if month < 1 or month > 12:
#         print("Error: Invalid month")
#     else:
#         if day < 1 or day > 31:
#             print("Error: Invalid day")
#         else:
#             if (month == 2 and day > 29) or \
#                (month in [4, 6, 9, 11] and day > 30):
#                 print("Error: Invalid day for the month")
#             else:
#                 formatted_year = str(year)[2:]
#                 print(f"{day}/{month}/{formatted_year.zfill(2)}")


# num1 = int(input("enter a number:"))
# num2 = int(input("enter a number:"))
# num3 = int(input("enter a number:"))
# if num1 > num2 and num3:
#     print(f"max number{num1}")
# elif num2 > num1 and num3:
#     print(f"max number{num2}")
# elif num3 > num1 and num3:
#     print(f"max number{num3}")


# computers = int(input("enter numbers of computers: "))
# if computers == "": #means in case no numbers is inserted
#     computers = 15
# else:
#     computers = int(computers)
#
# print(computers*2)












