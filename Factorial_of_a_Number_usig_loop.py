# write a program to find the fctorial of a number using loop
num = int(input("Enter any number"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"The factorial of {num} is {fact}")