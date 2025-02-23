
# try:
#     num = int(input("enter number: "))
#     print(num/0)
# except ValueError:
#     print("invalid number")
# except ZeroDivisionError:
#     print("zero division")


grade = int(input("enter grade: "))
if grade < 0 or grade > 100:
    raise ValueError("invalid grade: must be between 0-100")


