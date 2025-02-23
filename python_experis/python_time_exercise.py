# import time
# current_time = time.localtime()
# print(current_time)



#exercise9.1
# import time
# from datetime import datetime
# def get_current_year():
#     current_time = time.localtime()
#     current_year = current_time.tm_year
#     return current_year
#
# def calculate_100_year(age):
#     current_year = get_current_year()
#     year_100 = current_year + (100 - age)
#     return year_100
#
# def main():
#     name = input("enter your name: ")
#     age = int(input("enter your age: "))
#     year_100 = calculate_100_year(age)
#     current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#     print(f"hey, {name}")
#     print(f"you are {age} years old")
#     print(f"today's date is: {current_date}")
#     print(f"you will turn 100 years old in the year: {year_100}")
#
# main()



#exercise9.2
# from datetime import datetime
# current_date = datetime.now()
# european_format = current_date.strftime("%d/%m/%Y")
# american_format = current_date.strftime("%m/%d/%Y")
# print(f"European format: {european_format}")
# print(f"American format: {american_format}")


#exercise9.3
# from datetime import datetime
# def convert_to_date(birth_date_str):
#     birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y").date()
#     return birth_date
# birth_date_str = input("enter your birthdate (in DD/MM/YYYY format): ")
# birth_date = convert_to_date(birth_date_str)
# print(f"your birthdate as a date object is: {birth_date}")



#exercise9.4
from datetime import datetime
# def get_day_of_week(day_num):
#     days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     if 1 <= day_num <= 7:
#         return days[day_num - 1]
#     else:
#         return "invalid input, please enter a number between 1-7"
# day_num = int(input("enter a number between 1-7: "))
# day_name = get_day_of_week(day_num)
# print(f"the day corresponding to number {day_num} is: {day_name}")