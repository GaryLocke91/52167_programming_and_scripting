#This program asks the user to input any positive interger and outputs the successive values following a particular calculation

#Asks the user to input a positive interger
user_input = input("Please enter a positive integer: ")
num = int(user_input)
print(num)

#Runs a while loop until the value of the variable is 1
while num > 1:
    #If the value is even, it is divided by 2
    if (num % 2) == 0:
        num = int(num/2)
    #Otherwise, the value is multiplied by 3 and added to 1
    else:
        num = (num * 3) + 1
    print(int(num))
