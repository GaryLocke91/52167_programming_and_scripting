user_input = input("Please enter a positive integer: ")
num = int(user_input)
print(num)
while num > 1:
    if (num % 2) == 0:
        num = int(num/2)
    else:
        num = (num * 3) + 1
    print(int(num))
