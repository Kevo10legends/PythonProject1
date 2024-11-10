# while loop
# an increamental loop
num=2
while num<=15:
    print(f"loop:{num}")
    num+=2

# create a while loop with initioal 100 to 0 with decreasing with 5

num1=100
while num1>=0:
    print(num1)
    num1-=5

# for loop
name=["kevin","eric","mick","john","cloudia"]

for i in name:
    print(i)

num=[2,3,5,65,4,3,5,46]
total=0
for n in num:
    total+=1
print(f"The total of the elements is :{total}")

num=[2,3,5,65,4,3,5,46]
total=0
for n in num:
    total+=n
print(f"The total sum of the elements is :{total}")

myschool="emobilis"
for m in myschool:
    print(m)

num=[2,3,5,65,4,3,5,46]
for n in num:
    print(n)

numbers=[1,2,3,4,5,6,7,8,9,10]
evens=[]
for n in numbers:
    if n%2==0:
        evens.append(n)
    print(evens)