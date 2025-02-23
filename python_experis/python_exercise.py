#exercise 1.1
# a = 10
# b = 5
# sum = a+b
# print(f"the sum is: {sum}")

#exercise 1.2
# exercise 1.2
# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# current_year = int(input("What year is it?: "))
# years = 100 - age
# future = current_year + years
# print(f"In the year {future}, {name} will be 100 years old.")

#exercise 1.3
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# sum = num1+num2
# multi = num1*num2
# modulu = num1 % num2
# print(f"the numbers sum is: {sum} \n the numbers multi is: {multi} \n the numbers modulu is: {modulu} ")


#exercise 1.4
# current_salary = float(input("Enter your current salary: "))
# percentage_increase = float(input("Enter the percentage increase in salary: "))
# updated_salary = current_salary * (1 + percentage_increase / 100)
# print(f"Your updated salary after the increase is: {updated_salary:.2f}")

#exercise 1.5
# PI = 3.14
# radius = float(input("enter the radius of the circle: "))
# circumference = 2 * PI * radius
# area = PI * radius * radius
# print(f"the circumference of the circle is: {circumference:.2f}")
# print(f"the area of the circle is: {area:.2f}")


#exercise 2.1
# num1 = int(input("enter a number: "))
# if num1 % 2 == 0:
#     print(f"{num1} is even")
# else:
#     print(f"{num1} is odd")


#exercise 2.2
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))
# if num1 > num2 and num1 > num3:
#     print(f"{num1} is the largest number")
# if num2 > num1 and num2 > num3:
#     print(f"{num2} is the largest number")
# if num3 > num1 and num3 > num2:
#     print(f"{num3} is the largest number")


#exercise 2.3
# fixed_computers = int(input("how many computers fixed today?: "))
# if fixed_computers < 0:
#     print("15 computers")
# else:
#     print(f"{fixed_computers} got fixed today")
# to_be_fixed = fixed_computers*2
# print(to_be_fixed)


#exercise 3.1
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# if num1 > num2:
#     num1, num2 = num2, num1 #the code will swap the numbers if num2 is larger than num1
# print(f"Even numbers between {num1} and {num2} (not including them):")
# for i in range(num1 + 1, num2):
#     if i % 2 == 0:
#         print(i)


#exercise 3.2
# num = int(input("enter a number: "))
# for i in range(2,(num//2)+1):
#     if num % i == 0:
#         print(f"{num} is not prime number")
#         break
# else:
#     print(f"{num} is prime number")


#exercise 3.3
# from random import randint
# number = randint(1, 10)
# print(number)
# while True:
#     user = int(input("guess the number: "))
#     if number == user:
#         print("bravo you guessed it right:)")
#     elif number > user or user > number:
#         print("you got the wrong one try again")


#exercise 3.4
# print("Think of a number between 1 and 100, and I will try to guess it.")
# input("Press Enter when you're ready!")
#
# low = 0
# high = 9
#
# while True:
#     guess = (low + high) // 2
#     print(f"My guess is: {guess}")
#     user_input = input("Is my guess too high, too low, or correct? (h/l/c): ").lower()
#
#     if user_input == 'c':
#         print(f"Yay! I guessed your number: {guess}")
#         break
#     elif user_input == 'h':
#         high = guess - 1  # The guess was too high, so adjust the range
#     elif user_input == 'l':
#         low = guess + 1  # The guess was too low, so adjust the range
#     else:
#         print("Invalid input. Please enter 'h' for high, 'l' for low, or 'c' for correct.")


#exercise 3.5
# num1 = 0
# num2 = 1
# number_of_prints = int(input("enter a number:" ))
# for i in range(number_of_prints):
#     if num1 == 0 and i == 0:
#         print(num1)
#     if i!=0:
#         num3 = num1 + num2
#         print(num3)
#         num2=num1
#         num1 = num3



#exercises from the link
#exercise 2
# num = int(input("enter a number: "))
# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


#exercise 3
# num = int(input("Enter a number: "))
# total_sum = sum(range(1, num + 1))
# print(f"The sum of all numbers from 1 to {num} is: {total_sum}")


#exercise 4
# num = int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")


#exercise 6
# num = int(input("enter a number: "))
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# print(f"the total number of digits is: {count}")



#exercise 7
# num = int(input("enter a number: "))
# for i in range(5,0,-1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()


#exercise 11
# num = int(input("enter a number: "))
# for i in range(2, (num//2)+1):
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")



#exercise 14
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # stat from index 1 with step 2( means 1, 3, 5, an so on)
# for i in my_list[1::2]:
#     print(i, end=" ")
