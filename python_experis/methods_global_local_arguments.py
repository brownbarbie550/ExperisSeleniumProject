def method1():
    global a #changes the parameter that outside the function and in the main
    a += 5
    print(a)

a = 10
method1()
print(a)