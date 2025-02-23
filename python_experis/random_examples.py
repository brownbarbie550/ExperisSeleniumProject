from random import randint

#get 10 random prices and print expensive/not expensive (expensive>=200)
for i in range(5):
    price = randint(1,500)
    print(price)
    if price >= 200:
        print("very expensive")
    else:
        print("not expensive.....")


