#exercise 1
# sum_numbers = 0
# for num in range(6):
#     num = int(input("enter a number: "))
#     sum_numbers += num
#     average = sum_numbers / 6
# print("the sum of the numbers is:", sum_numbers)
# print("the average is:", average)

#exercise 2
# sum_numbers = 0
# num_counter = 0
# odd_counter = 0
# for num in range(6):
#     num = int(input("enter a number: "))
#     if num % 2 == 0:
#         sum_numbers += num
#         num_counter += 1
#     elif num % 2 != 0:
#         odd_counter += 1 #add here a counter for the odd ones too
#
# print("the sum of the numbers is:", sum_numbers)
# print("the average is:", sum_numbers / num_counter)
# print("the odd numbers are:", odd_counter)

#exercise 3
# for num in range(10,100):
#     if num % 10 == 7 or num // 10 == 7:
#         print(num)

#exercise 4
# sum_num = 0
# for num in range(10,100):
#     if num % 10 == 0:
#         sum_num += num
#     print(num)
# print("the sum of the numbers that end with 0 are:", sum_num)


#exercise 5
# grades = int(input("enter grade: "))
# sum_of_passed_grades = 0
# sum_of_negative_grades = 0
# counter_of_passed_grades = 0
# counter_of_negative_grades = 0
# while 0 == grade <= 100:
#     if grade >= 60:
#         sum_of_passed_grades += grade
#         counter_of_passed_grades =+ 1
#     else:
#         sum_of_negative_grades += grades
#         counter_of_negative_grades += 1
#     grade = int(input("enter grade: "))
# if counter_of_passed_grades > 0:
#     print("average of grades is:", sum_of_passed_grades / counter_of_passed_grades)
# else:
#     print("no passed grades.")
# if counter_of_negative_grades > 0:
#     print("average of failed grades:", sum_of_negative_grades / counter_of_negative_grades)
# else:
# #     print("no failed grades")
#
# exercise 7
# from random import randint
# total_num = 0
# for i in range(5):
#     number = randint(0,100)
#     print(f"{i+1} , {number}")
#     total_num += number%10
# print(f"numbers sum: {total_num}")

#exercise 8
# num1 = int(input("enter a number: "))
# for i in range(1,num1+1):
#     if i % 5 == 0:
#         print(i)

#exercise 9
# num1 = int(input("enter a number: "))
# for i in range(2,num1+1, 2):
#     # if i % 2 == 0:
#         print(i)


#exercise 10
# counter = 0
# num = int(input("enter a number: "))
# while num != 0:
#     if num % 7 == 0 or num % 3 == 0:
#         counter += 1
#     num = int(input("enter a number: "))
# print(counter)


#extra_exercises
# num1 = int(input("enter a number: "))
# for i in range(1, num1+1):
#     if i % 7 == 0:
#         print("BOOM")
#     else:
#         print(i)


# from random import randint
# total = 0
# counter = 0
#
# for i in range(7):
#     price = randint(1,100)
#     print(f"product number {i+1}: {price}")
#
#     if total+price < 300:
#         total += price
#         counter += 1
#         print(f"total: {total}, counter: {counter}")
#     else:
#         print(f"the product is expensive")
#
# print("total", total)
# if counter > 0:
#     print("average:", total / counter)
# else:
#     print("no products were purchased")

















