#This program determines if today is a weekday or not
#Imports the datetime module
import datetime
#Stores the current date and time in a variable
now = datetime.datetime.now()
#Returns the day of the week as an interger
x = now.weekday()
#If x is less than 5, it's a weekday
if x < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")