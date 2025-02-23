
#while loops exercise

#exercise1
# num = int(input("enter a number: "))
# while 100 <= num <= 999:
#     a = num % 10
#     b = num // 10 % 10
#     c = num // 100
#     sum_num = a+b+c
#     print(sum_num)
#     num = int(input("enter a number: "))
# print("its not 3 digits")


# exercise2
# while age >= 0 and age <= 120:
# while 0 <= age <= 120:
#     if age <= 18:
#         print("child")
#     elif age <= 60:
#         print("adult")
#     else:
#         print("senior")
#     age = int(input("enter your age: "))
# print("invalid age")

# exercise3
# num1 = int(input("enter a number: "))
# num2 = int(input("enter another number: "))
#
# while num1 % 2 == 0 and num2 % 2 == 0:
#     print(num1+num2)
#     num1 = int(input("enter a number: "))
#     num2 = int(input("enter another number: "))
# print(num1*num2)


#exercise4
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
#
# while num1+num2 == 10:
#     num1 = int(input("enter a number: "))
#     num2 = int(input("enter a number: "))
# print("session ended")


#exercise5
# number = int(input("enter your favorite number: "))
# while 10 <= number <= 99:
#     a= number % 10
#     b = number // 10
#     if number % 7 == 0 or a == 7 or b == 7:
#         print("lucky number")
#     else:
#         print("not a lucky number")
#     number = int(input("enter your favorite number: "))

# count = 0
# grade = int(input("enter grade: "))
#
# while grade < 0 or grade > 100:
#     print("invalid grade")
#     count += 1
#     if count == 3:
#         print("too many trials")
#         break
#     grade = int(input("enter grade: "))
#
# else:
#     if grade >= 70:
#         print("passed")
#     else:
#         print("failed")
# print(f"number of invalid trails: {count}")


# count = 0
# price = int(input("enter price: "))
#
# while price > 0:
#     if price >= 200000:
#         print("I'm not staying here!!!!")
#         break
#     count += 1
#     if price >= 200:
#         print("Very expensive!")
#     else:
#         print("not expensive...")
#     price = int(input("enter price: "))
#
# else:
#     print(f"Thank you for my shopping. Number of products: {count}")
