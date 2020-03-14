#This program calcluates the square root of a number
#Imports the math module
import math

#Asks the user to input a positive number
num = float(input("Please enter a positive number: "))

#Defines the function (sourced from https://helloacm.com)
def sqrt(x):
    sgn = 0
    if x < 0:
        sgn = -1
        x = -x
    val = x
    while True:
        last = val
        val = (val + x / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    if sgn < 0:
        return complex(0, val)
    return(val)

#Calls the function and assigns it to a variable
sqrt_num = sqrt(num)

#Outputs the result rounded to one decimal place
print("The square root of ", num, "is approx. ", round(sqrt_num, 1))