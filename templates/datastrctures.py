# list,index,mutable(changeble)

cars=["Toyota","BMW","Mercedes","Subaru"]
num=[6,9,57,0,-6,3,54]
num.sort()


cars[1]="Infinity"
cars.sort()

print(cars)
print(f"I love driving {cars[1]}")
print(num)

# tuple, index,immutable(unchangeble),ordered

fruits=("mangoes","bananas","oranges","watermelons")
# fruits[2]="oranges"
print(fruits)
print(fruits[2])

# set

color={"red","blue","green","white"}
print(color)

# dictionary

employees={"name":"kevin","age":18,"salary":536753}
print(employees)
print(f" The age of {employees['name']} is: {employees['age']}")