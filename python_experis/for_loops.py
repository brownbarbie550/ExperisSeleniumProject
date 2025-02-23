
# for i in range(1,101):
#     print("brown barbie", i)
#
# for i in range(101):
#     print("brown barbie", i)

# for i in range(10,50,3):
#     print("brown barbie", i)

# for i in range(100,70,-1):
#     print("brown barbie", i)

# for i in range(100,70,-5):
#     print("brown barbie", i)

#get 5 prices from the user and print expensive/not expensive (expensive: >=200)
# for i in range(5):
#     price = int(input("enter price: "))
#     if price >= 200:
#         print("very expensive!")
#     else:
#         print("not expensive.....")


#go through all the numbers between 1-100 and print the numbers that are divided by 4.
# for i in range(1,101):
#     if i % 4 == 0:
#         print(i)
# print("################################")
# for i in range(4,101,4):
#     print(i)


#get two number from the user
#go through all the numbers between and print the numbers that are divided by 4.
# num1  = int(input("enter a number: "))
# num2  = int(input("enter a number: "))
# for i in range(num1,num2+1):
#     if i % 4 == 0:
#         print(i)



#for_loops_exercise
#exercise1
# for i in range(5):
#     num = int(input("enter a number: "))
#     if 100 <= num  <= 999:
#         print(num % 10 + num // 10 % 10 + num // 100)
#     else:
#         print("invalid number")


#exercise2
# from random import randint
# for i in range(10):
#     age = randint(0,120)
#     print(age)
#     if age <= 18:
#         print("child")
#     elif age <= 60:
#         print("adult")
#     elif age <= 120:
#         print("senior")

#exercise3
# from random import randint
# for i in range(12):
#     a = randint(0,50)
#     b = randint(0,50)
#     print(f"a: {a} b: {b}")
#     if a % 2 == 0 and b % 2 == 0:
#         print(a+b)
#     if a % 2 == 0 or b % 2 == 0:
#         print(a*b)


#exercise4
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# for i in range(num1, num2+1):
#     if i % 4 == 0:
#         print(i)


#exercise5
# from random import randint
# user_num1 = randint(10,99)
# user_num2 = randint(10,99)
#
# print(f"this is the numbers: number 1:{user_num1} number 2:{user_num2}")
# if user_num1 > user_num2:
#     biggest_num = user_num1
#     smallest_num = user_num2
# else:
#     biggest_num = user_num2
#     smallest_num = user_num1
#
# for i in range(smallest_num,biggest_num + 1):
#     if i % 7 == 0 or i //10 ==7 or i % 10 == 7:
#         print(f"lucky number is: {i}")

