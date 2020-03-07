#This program calcluates the square root of a number

import math

#Asks the user to input a positive number
num = float(input("Please enter a positive number: "))

#Defines the function which takes one input and uses the appropriate method in the math module
def sqrt(x):
    ans = math.sqrt(x)
    return(ans)

#Calls the function and assigns it to a variable
sqrt_num = sqrt(num)

#Outputs the result rounded to one decimal place
print("The square root of ", num, "is approx. ", round(sqrt_num, 1))