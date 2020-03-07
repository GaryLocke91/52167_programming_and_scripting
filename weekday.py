#This program determines if today is a weekday or not

import datetime

#Returns the day of the week using the appropriate method in the datetime module
now = datetime.datetime.now()
x = now.weekday()

#If x is less than 5, it's a weekday and the appropriate message is printed
if x < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")