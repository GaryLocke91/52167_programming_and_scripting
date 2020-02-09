#This program calculates a person's Body Mass Index (BMI)

#Asks the person to input their weight and height
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter hegiht in centimetres: "))
#Divides the person's weight by their height in metres squared
bmi = weight/((height/100)**2)
#Outputs the person's BMI rounded to one decimal place
print("BMI is: ", round(bmi, 1))
