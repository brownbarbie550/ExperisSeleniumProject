text = "i am learning python"

list1 = text.split()  #split the sentence into a list
print(list1)

text = "14,15,16,17,18,19"
list1 = text.split(",")
print(list1)

#create from the text above a list of numbers
list1 = [int(i) for i in text.split(",")]
print(list1)

