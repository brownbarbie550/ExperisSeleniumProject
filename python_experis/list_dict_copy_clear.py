list1 = [10,20,30,40,50,60,70]

list2 = list1   #list1 and list2 are the same list now
list1.append(70)
print("list1:", list1)
print("list2:", list2)

list3 = list1.copy()
list3.append(80)
print("list3:", list3)
print("list1:", list1)

list3 = []  #list3 will be a new empty list

list2.clear()   #clear list2 (the memory address is not changed)