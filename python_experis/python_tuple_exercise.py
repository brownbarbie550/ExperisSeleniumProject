# tuple_one = ()  #this how tuple is defined
# tuple1 = (10,20,30,40,50,100)
# tuple2 =  10,20,30,40,50,100
#          0  1  2  3  4  5
#both are tuple
#
# print(type(tuple1))
# print("tuple1[2]", tuple1[2])
#
# tuple1 += (100,200,300)
# print(tuple1)
# tuple1 += 400, #in order for python to understand that this is a tuple ',' need to be added
# print(tuple1)


#in order to update the tuple we converted it to listed updated and converted it back to tuple
# list1 = list(tuple1)
# print(list1)
# list1[0] = 11
# print(list1)
# tuple1 = tuple(list1)
# print(tuple1)



#exercise 6.4
# from random import randint
# list1 = []
# for i in range(10):
#     nums = randint(1,100)
#     list1.append(nums)
# print(list1)
# print(tuple(list1))
# user_input = input("enter a number: ")
# list1.append(user_input)
# tuple1 = tuple(list1[0:4] + list1[5:10])
# print(tuple1)








