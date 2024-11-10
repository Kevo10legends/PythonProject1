# create a programme that checks if a number is odd or even
num=int(input("Enter a number:"))

if num % 2 ==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# create a programme tha ckecksmif someone can vote or not

age=int(input("Enter your age:"))
if age >=18:
    print("You can vote")
else:
    print("Failed.You cant vote")

# create a programme that checks a student grade

grade=int(input("Enter your marks:"))

if grade >=70:
    print("You got an A")
elif grade >=60:
    print("You got a B")
elif grade >=50:
    print("You got a C")
elif grade >=40:
    print("You got a D")
elif grade <=39 and grade ==0:
    print("You got an F")
else:
    print("Wrong input")

# create a programme to calculate your BMI
