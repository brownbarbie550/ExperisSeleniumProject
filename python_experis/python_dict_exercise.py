#exercise 7.1
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4 = {}
# dict4.update(dict1)
# dict4.update(dict2)
# dict4.update(dict3)
# print(dict4)


#exercise 7.2
# dict1 = {"shirt":200, "shoes":400, "jacket":350, "pants":150, "dress":200, "coat":150}
# if "shoes" in dict1:
#     print("shoes exists")
# else:
#     print("no shoes in dict1")

#exercise 7.3
# dict1 = {"shirt":200, "shoes":400, "jacket":350, "pants":150, "dress":200}
# switched_dict1 = {}
# for key, value in dict1.items():
#     switched_dict1[value] = key
# print(dict(switched_dict1))


#exercise 7.4
# user_num = int(input("enter a number: "))
# dict_one = {}
# for i in range(user_num):
#     dict_one[i]= i*i
# print(dict_one)


# #exercise 7.5
# dict1 = {"shirt":200, "shoes":400, "jacket":350, "pants":150, "dress":200}
# values = dict1.values()
# print(sum(values))

#exercise 7.6
# user_input = input("enter a key: ")
# dict1 = {"shirt":200, "shoes":400, "jacket":350, "pants":150, "dress":200, "coat":150}
# if user_input in dict1:
#    dict1.pop(user_input)
# print(dict1)

#exercise 7.7
# dict1 = {"shirt":200, "shoes":400, "jacket":350, "pants":150, "dress":200, "coat":150}
# unique_dict = {}
# for key, value in dict1.items():
#     if value not in unique_dict.values():
#         unique_dict[key] = value
# print(unique_dict)

#exercise 7.8
# name_list = ["Tokyo", "Rio", "Denver", "Berlin", "Paris"]
# grade_list = [100,70,90,98,74]
# diction = {}
# for i in range(len(name_list)):
#     diction[name_list[i]] = grade_list[i]
# print(diction)





#more exercises in the python classer page 144 check it