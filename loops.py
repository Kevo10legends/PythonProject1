# #while loop
#
# num=2
#
# while num<=15:
#     print(f"loop: {num}")
#     num+=2
#     #       An incremental loop
#
#
#
#
#     # for loop
#     name=["kevin","erick","michael","cloudia"]
#     for i in name:
#         print(i)
num=[2,5,89,2,8,8,1,9,3]
total=0
for n in num:
            total+=n
print(f"The total of the element is :{total}")
#even numbers
numbers=[ 1,2,3,4,5,6,7,8,9,10 ]
even=[]
for num in numbers:
         if num % 2==0:
            even.append(num)

print(even)