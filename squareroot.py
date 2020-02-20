#This program calcluates the square root of a number

#Imports the math module and ask the user for input
import math
num = float(input("Please enter a positive number: "))

#Defines the function which takes one input
def sqrt(x):
    #Uses the appropriate method in the math module for the calculation
    ans = math.sqrt(x)
    return(ans)

#Calls the function and assigns it to a variable
sqrt_num = sqrt(num)
#Outputs the square root of the number rounded to one decimal place
print("The square root of ", num, "is approx. ", round(sqrt_num, 1))