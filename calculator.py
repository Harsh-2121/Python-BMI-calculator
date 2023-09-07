print("BMI Calculator")
print("BMI is Body Mass Index. A very high number may indicate that you are overweight.")
print("This calculator will reliably calculate your BMI using your weight and height.")
# Input height, weight, and age
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
age = int(input("Enter your age: "))
# Calculate BMI
bmi = weight / (height ** 2)
# Print the result
print(f"Your BMI is: {bmi:.2f}")
# Check BMI ranges
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("Your weight is in the healthy range.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
