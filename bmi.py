#This program calculates a person's Body Mass Index (BMI)

#Asks the user to input the weight and height values
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter hegiht in centimetres: "))

#Divides the weight by the height in metres squared
bmi = weight/((height/100)**2)

#Outputs the calculation rounded to one decimal place
print("BMI is: ", round(bmi, 1))
