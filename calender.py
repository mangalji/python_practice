
# import calendar
# year = 2026
# month = 4
# print(calendar.month(year,month))


import calendar

print("Calender Program")
year = int(input("enter the year: "))
month = int(input("enter the month in digits(1-12): "))

print("\nHere is the calendar: \n")
try:
	print(calendar.month(year,month))
except IndexError:
	print("you are given wrong input!!!")
	print("please enter correct input next time...")