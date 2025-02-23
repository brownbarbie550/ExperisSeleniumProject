
# dict1 = {"shirt":200, "shoes":400, "jacket":350, "pants":150, "dress":200}
# print('dict1["jacket"]:', dict1["jacket"])

#add key:value to the dictionary
# dict1["shirt"] = 150
# print(dict1)

#update a value of an existing key
# dict1["shoes"] = 450
# print(dict1)

#remove key:value from the dictionary
# del dict1["shoes"]
# print(dict1)

#add the new key and remove the old key
# dict1["tshirt"] = dict1["shirt"]
# print(dict1)
# del dict1 ["shirt"]
# print(dict1)

# print("len(dict1):", len(dict1))
# print("max(dict1):", max(dict1))
# print("min(dict1):", min(dict1))
# print("sum(dict1):", sum(dict1)) #it will sum the keys, it wont sum here cause the keys are strings


#check if key exists
# if "tshirt" in dict1:
#     print("tshirt is available")

#it doesn't work for value
# if 150 in dict1:
#     print("150 exists")


#go through the dictionary: go through the keys
# for product in dict1:
#     print(f"{product}: {dict1[product]}")


# grades = {"Liri":75, "Daniel":40, "Barel":55, "Evyatar":99, "Liron":82, "Kate":74}
#go through the dictionary: every failed grade -> add 10%
# for name in grades:
#     if grades[name] < 70:
#         grades[name] = grades[name]*1.1
# print(grades)


#add dictionary to a dictionary
# grades.update({"Lea":100, "Daniel":95, "Raz":88})
# print(grades)
# grades2 = {"Michal":79, "Dagmawit":90}
# grades.update(grades2)
# print(grades)

#get all the values that exists in a dictionary
# print("grades.values()", grades.values())
#print the values in a list
# values = list(grades.values())
# print("list of the values:", values)

#get the average grade
# print("average:", sum(values)/len(grades))

# #check if we have grade 100
# if 100 in values:
#     print("someone got 100")


#find the names that get 100
# for name in grades:
#     if grades[name] == 100:
#         print(f"{name} got 100")




#create a grades dictionary: name:grade (of10 items)
#we will get the names as inout from the user
#the grades will be created randomly

# from random import randint
# grades = {}
#
# for i in range(10):
#     name = input("enter a name: ")
#     grade = randint(20,100)
#     grades[name] = grades
#     grades.update({name:grade})
#
# print(grades)
# print(grades.values())
# print("average:", sum(grades.values())/ len(grades))
#
# print(grades.keys())
#
# print(list(grades))
#
# print(grades.items()) #returns a list which in every block the items are in a tuple
#
# for i in grades.items(): #does the same but prints them in order
#     print(i)


# grades = {"Liri":75, "Daniel":40, "Barel":55, "Evyatar":99, "Liron":82, "Kate":74}
#
# brilliant_grades = {}
# failed_grades = {}
# for name in grades:
#     if grades[name] > 60:
#         brilliant_grades[name] = grades[name]
#     else:
#         failed_grades[name] = grades[name]
# print("brilliant:", brilliant_grades)
# print("failed:", failed_grades)