# BMI Calculator

# Get user input for weight and height
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI result
print(f"Your BMI is: {bmi:.2f}")

# Interpret BMI result
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print(f"BMI Category: {category}")
