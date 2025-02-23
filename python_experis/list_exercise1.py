#print random numbers in a list
# from random import randint
# list_one = []
# num = int(input("enter a number:"))
# for i in range(20):
#     random_nums = randint(1,50)
#     list_one.append(random_nums)
#     if num in random_nums:
#         list_one.remove(num)
# print(list_one)
import random
#print random numbers then receive a number from the user
#and if that number is on the list it will be removed
# from random import randint
# one_list = []
# for i in range(20):
#     random_nums = randint(1,50)
#     one_list.append(random_nums)
# print(one_list)
# num = int(input("enter a number:"))
# while num in one_list:
#     one_list.remove(num)
# print(one_list)


#python exercises-lists
#exercise 1
# from random import randint
# list1 = []
# for i in range(10):
#    rand_nums = randint(1,100)
#    list1.append(rand_nums)
# print(list1)


#exercise 2
# list_one = [1,2,3,4,5,6,7,8,9,10]

#exercise 3
# list_one = [1,2,3,4,5,6,7,8,9,10]
# list1 = []
# list1.append(list_one[7:10])
# print(list1)


#exercise 4
# list_one = [1,2,3,4,5,6,7,8,9,10]
# print(list_one[::-1])


#exercise 5
# list_one = [1,2,3,4,5,6,7,8,9,10]
# index = list_one[::2]
# print(index)


#exercise 6
# list_one = [1,2,3,4,5,6,7,8,9,10]
# lislist = []
# lislist.append(list_one[0:3])
# print(lislist)



#exercise 7
# list_one = [1,2,3,4,5,6,7,8,9,10]
# for num in list_one:
#     if num % 2 != 0:
#         print(num)



#exercise 8
# user_num = int(input("enter a number: "))
# list_one = [1,2,3,4,5,6,7,8,9,10]
# if user_num > 0:
#     list_one[7:9] = [user_num, user_num]
# print(list_one)


#exercise 9
# user_num = int(input("enter a number: "))
# list_one = [1,2,3,4,5,6,7,8,9,10]
# if user_num:
#     list_one[7:9] = [user_num, user_num]
# print(list_one)



#exercise 10
# list_one = [1,2,3,4,5,6,7,8,9,10]
# remo_list = []
# for num in list_one:
#     if num % 3 == 0:
#         list_one.remove(num)
#         remo_list.append(num)
# print(list_one)
# print(remo_list)



#exercise 11
# the_list = [1,1,2,3,5,8,13,21,34,55,89,144]


#exercise 12
# user_str = input("type in something: ")
# unique_words = []
# for char in user_str:
#     if char not in unique_words:
#         unique_words.append(char)
# print(unique_words)


#exercise 13
# from random import randint
# user1 = int(input("enter a number: "))
# num_list = []
# for i in range(20):
#     rand_nums = randint(1,100)
#     num_list.append(rand_nums)
#     # print(num_list)
#     for num in num_list:
#         if num == user1:
#             print(f"{num} is in num_list")
#             num_list.remove(num)
# print(num_list)



#exercise 14
# user_num = int(input("enter a number: "))
# divisors = []
# for i in range(1, user_num + 1):
#     if user_num % i == 0:
#         divisors.append(i)
# print(f"the divisors of {user_num} are: {divisors}")



#exercise 15
# user1 = int(input("how many fibonnaci numbers to generate: "))
# fibo_list = [1,1]
# for i in range(2, user1 + 2):
#     fibo_list.append(fibo_list[i-2]+fibo_list[i-1]) #recursion
# print(fibo_list)



#exercise 16
# the_list = [1,1,2,3,5,8,13,21,34,55,89,34,144]
# list_one = []
# for num in the_list:
#     if num not in list_one:
#         list_one.append(num)
# print(list_one)



#exercise 17
# the_list1 = [1,1,2,3,54,88,13,21,34,55,89,34,144]
# the_list2 = [11,4,22,38,5,8,13,21,34,55,9,34,144]
# for num in the_list1:
#      if num in the_list1 and num in the_list2:
#          print(f"the two list got number {num} in common")



#exercise 18
# user_str = input("type in something: ")
# str_list = []
# for i in user_str:
#     str_list.append(user_str)
# count = 0
# for string in str_list:
#     if len(string) >= 4 and str_list[0] == str_list[-1]:
#         count +=1
# print(f"number of strings that meet the criteria: {count}")



#exercise 19
# from random import randint
# num_list = []
# for i in range(10):
#     rand_num = randint(1, 20)
#     num_list.append(rand_num)
#     print(rand_num)
#
# digit_count = [0] * 10
#
# for num in num_list:
#     for digit in str(num):
#         digit_count[int(digit)] += 1
#
# for i in range(10):
#     if digit_count[i] > 0:
#         print(f"Digit {i} appears {digit_count[i]} times")




#exercise 20
# from random import randint
# num_list = []
# # num_list = [randint(1, 20) for _ in range(10)]
# for i in range(10):
#     rand_num = randint(1,20)
#     num_list.append(rand_num)
# print("Generated list of numbers:", num_list)
#
# user_input = int(input("Enter a number to find its index: "))
# # found = False  # Flag to track if the number was found
# for i in range(len(num_list)):
#     if num_list[i] == user_input:
#         print(f"The number {user_input} is found at index {i}.")
#         break
# else:
#     print(f"The number {user_input} was not found in the list.")


#exercise 21
# from random import randint
# digits = list(range(10))
# random.shuffle(digits)
# secret_number = ''.join(str(digits[i])for i in range(4))
#
# while True:
#     guess = input("enter your guess (4 unique digits): ")
#     if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
#         print("invalid guess, please enter exactly 4 unique digits")
#         continue
#
#     bulls = 0
#     hits = 0
#     for i in range(4):
#         if guess[i] == secret_number[i]:
#             bulls += 1
#         elif guess[i] in secret_number:
#             hits += 1
#     print(f"Bulls: {bulls}, Hits: {hits}")
#
#     if bulls == 4:
#         print(f"congratulations, you guessed the number: {secret_number}")
#         break






















