#exercise 4.1
# list1 = []
# user_num = int(input("enter a number: "))
# for i in range(user_num):
#     user_num = int(input("enter a number: "))
#     list1.append(user_num)
#     if user_num <= 0:
#         break
# if list1:
#     print("the max number is: ", max(list1))
#     print("the min numbers is: ", min(list1))
#     print(min(list1) + max(list1) / 2)


#exercise 4.2
# user = input("type in something: ")
# print(user[::-1])


#exercise 4.3
# from random import randint
# num_list = []
# for i in range(10):
#     random_nums = randint(1,50)
#     num_list.append(random_nums)
# print(num_list)


#exercise 4.4
# list1 = []
# list2 = []
# big_list1 = []
# user1 = (input("enter for the first list: "))
# user2 = (input("enter for the second list: "))
# list1.append(user1)
# print(list1)
# list2.append(user2)
# print(list2)
# big_list1 = list1 + list2
# print(f"the big and combined list: {big_list1}")



# #exercise 4.5
# grades_list = []
# count_high = 0
# count_low = 0
#
# while True:
#     grades = int(input("enter your grade: "))
#     if grades < 0:
#         break
#     if grades > 60:
#         count_high+=1
#     else:
#         count_low+=1
# print(grades)
# print(f"grades above 60: {count_high}")
# print(f"grades below 60: {count_low}")


#exercise 4.6
# the_list = [1,2,3,4,5,6,7,8,9,10]
# list_one = []
# list1 = []
# list_one.append(the_list[:-4:-1])
# list1.append(the_list[0:10:2])
# print(list_one)
# print(list1)
# print("answer for b:", the_list[::-1])
# print("answer for c:", the_list[1:10:2])

#answer for e
# user_num1 = int(input("enter a number: "))
# user_num2 = int(input("enter a number: "))
# user_num3 = int(input("enter a number: "))
# new_list = the_list[1:4] + [user_num1+user_num2]+ the_list[6:]+[user_num3]
# print(new_list)



#answer for f
# list_list = []
# for i in the_list:
#     list_list.append(i*2)
# print(list_list)


#answer for g
# another_list = [the_list[0], the_list[-1]]
# print(the_list)







#extra exercise
#ליצור רשימה של 20 מספרים אקראיים, לעבור עליה וליצור ממנה רשימה של מספרים שמתחלקים ב-7.
# num_list = [10,9,20,15,21,6,11,8,78,10,7,12,23,63,4,16,70,48,19,94]
# list = []
# for i in num_list:
#     if i % 7 == 0:
#         list.append(i)
# print(list)



# from random import randint
# lis_list = [randint(0,100)for i in range(10)]
# print(lis_list)
#
# list1 = []
# for i in lis_list:
#     if i not in list1:
#       list1.append(i)
# print(list1)

# from random import randint
# list_num = [randint(1,20) for i in range(10)]
# print(list_num)
# list_no_dup = []
# for item in list_num:
#     if item not in list_no_dup:
#         list_no_dup.append(item)
# print(list_no_dup)


#append and += adds to the list without changing it and = changes the list
