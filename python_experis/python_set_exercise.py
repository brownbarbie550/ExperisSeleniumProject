set1 = {1,2,3,4,5,6,7,8,9,14}
set2 = set() #define a new and an empty set
print(set1)
#if there are duplications then it won't be printed

# set1.add(15)
# print(set1)
#
# print(set1.pop()) #pops up a random item from the set and removes it too
# print(set1)

#set is mostly used when the priority is to have no duplication

# set1.remove(14)
# print(set1)


# set1.discard(8) #works the same as remove to delete an item but won't return error if given item that doesn't exist
# print(set1)
#
# set1.update({10,2,30,40})
# print(set1)

#convert it to a set which will remove all the duplications
# list1 = [1,2,3,4,5,6,7,2,4,1]
# set2 = set(list1)
# print(set2)
#convert it back to list
# list1 = list(set2)
# print(list1)

#works the same as the code above
# list1 = [1,2,3,4,5,6,7,2,4,1]
# print(list(set(list1)))



#exercise 8.4
#answer for a
# set1 = {1,2,3,4,5,6,7,18,10}
# set2 = {10,11,12,13,14,4,5,15,1}
#answer for b
# set3 = set()
# set3 = set1.union(set2)
# print(set3)
#answer for c
# set3.remove(15)
# print(set3)
#answer for d
# print(max(set3))
# print(min(set3))
# print(len(set3))
#answer for e
# set4 = set()
# set4 = set3
# print(set4)
#answer for f
# del set1
# del set2
