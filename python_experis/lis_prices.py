#get 6 valid prices from the user (>0)
#cvalculate total and average
#skip a product that is over 300
total = 0
counter = 0
prices = []
for i in range(6):
    price = int(input(f"enter price{i+1}: "))
    prices.append(price)

    while price < 0:
        print("invalid price!!!!")
        price = int(input(f"enter price{i + 1}: "))

    if price > 300:
        print("too expensive, i wont buy it")

    total += price
    counter += 1

print("total:", total)
if counter > 0:
    print("average:", total / counter)
else:
    print("no products were purchased")

print(prices)