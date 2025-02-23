#exercise1
# word = input("enter a word: ")
# word = word.replace("A", "a").replace("a", "")
# print(word)
from http.cookiejar import user_domain_match

# new_word = ""
# for i in word:
#     if i != "a" and i != "A":
#         # if i.lower != "a": #another way to do it
#         new_word += i
# print(new_word)
#its a way to build a word or string step by step but it depends on what we want to do


#exercise2
# user_str = input("type in something: ")
# for i in user_str:
#     print(user_str[0] + user_str[-1])




#exercise3
# user_str = input("type in something: ")
# user_letter = input("type in something: ")
# for i in range(len(user_str)):
#      if user_str[i] == user_letter:
#          index = i
#          print(index)
#          break
# else:
#     print("-1")



#exercise4
# user_str = input("type in a word: ")
# count = 0
# print(user_str)
# for i in user_str:
#     count+=1
# print(count)



#exercise5
# user_str = input("type in a word: ")
# user_letter = input("type in a letter: ")
# for i in user_str:
#     if i == user_letter:
#         print(user_str)


#exercise6
# user = input("type in a word: ")
# new_word = user[0].upper() + user[1::]
# print(new_word)



#exercise7
# user_input = input("enter a word: ")
# word = ""
# for i in user_input:
#     word += i*2
# print(word)


#exercise8
# user_input = input("type in something: ")
# char_count = {}
# for char in user_input:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] =1
# for char, count in char_count.items():
#     if count != 1:
#         print(char, end= "")


#exercise9
# user1 = input("enter a word: ")
# user2 = input("enter a word: ")
# count1 = 0
# counted_chars = []
# for i in user1:
#     if i in user2 and i not in counted_chars:
#         count1 +=1
#         counted_chars.append(i)
#         user2 = user2.replace(i, "", 1)
# if count1 > 0:
#     print(f"{count1} common characters found in both words that are{counted_chars}")
# else:
#     print("none found")




#exercise10
# import random
# from operator import indexOf
#
# codee = []
# user_name = input("Enter your name: ")
# password = ''.join(random.choice(user_name) for _ in range(6))
# print(f"Generated random password: {password}")



#exercise11
# sentence = input("type in a sentence: ")
# word = input("type in a word: ")
#
# words = sentence.split() #splits it into words
# list1 = [] #un empty list to store the words
# count = 0
# for w in words:
#     if word in w: #checks if the input word is a substring of the current word
#         list1.append(count)
#     count +=1
# if list1:
#     print(f"the word appears at: {list1}")
# else:
#     print("the word doesnt appear")




#exercise12
# user_input = input("enter a sentence: ")
# capitalized = user_input.title()
# print(capitalized)



#exercise13
# sentence = input("type in a sentence: ")
# letter = input("type in a letter: ")
# words = sentence.split()
# for word in words:
#     for w in word:
#         if w == letter:
#             new_word = w.capitalize()
#             print(new_word)
















# #exercise 5.4 from another file
# user_str = input("type in something: ")
# #questionA
# print(len(user_str))
# #questionB
# print(user_str[3:7])
#exerciseC
# words = user_str.split()
# if words:
#     first_word = words
#     print(str(first_word[0]))
#     print(str(first_word[0]))
#     print(str(first_word[0]))
# else:
#     print("no words found")

#questionD
# word = user_str.title() #capitalizes first letter of every word
# print(word)



