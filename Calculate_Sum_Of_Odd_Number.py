# write a program to calculate sum of odd number
sum = 0
num = int(input("Enter any number"))
for i in range(1,num+1):
    if i % 2 != 0:
        sum += i
print(sum)