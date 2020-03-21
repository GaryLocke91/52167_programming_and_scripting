#This program reads a text file and outputs the number of times the character 'e' occurs

#Asks the user to input a file name
file_name = input("Please enter a text file name: ")
e_count = 0

#Opens and reads the file, and stores it in a variable
with open(file_name) as f:
    read_data = f.read()
    #Loops through each character of each word and increments the count variable
    for i in read_data:
        if i == 'e' or i == 'E':
            e_count += 1               
print(e_count)