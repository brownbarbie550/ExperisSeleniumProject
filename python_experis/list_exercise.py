list1 = [1,2,3,4,5,100,100,100]
# index  0 1 2 3 4
print(list1)
print(list1[1])

#print(list[5]) #error because index is out of range
# list1[2] = 200   #change an item in the list (according to the index)
# print(list1)

#add an item to the list
# list1.append(15)  #append adds one item only
# print(list1)

#add a list to the list
# list1+=[10,20,30]
# print(list1)

#a list inside a list
# list1[3] = [1,2,3]
# print(list1)

#remove an item from a list
# list1.remove(20)   #remove an item according to its value
# print(list1)
#
# del list1[1]   #remove an item according to its index
# print(list1)

#duplicate a lisr by int
# print(list1*3)
# print(list1)

#check if a value exists in the list
# if 100 in list1:
#     print("100 exists in the list")
# else:
#     print("100 doesn't exists in the list")

#check if a value doesn't exist in the list
# if 100 not in list1:
#     print("100 doesnt exist in the list")
# else:
#     print("100 exists in the list")


#find how many times a value exists in the list
print("list1.count(100)", list1.count(100))

#find the length of a list
print("length of list1", len(list1))

#get the max value in a list
print("the max value in the list is:", max(list1))

#get the min value of the list
print("the min value of the list is:", min(list1))


