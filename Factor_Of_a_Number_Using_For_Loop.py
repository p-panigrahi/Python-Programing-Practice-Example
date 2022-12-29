# write a program to find the factor of a number using for loop
num = int(input("Enter any number"))
print(f"The Factor of {num} is")
for i in range(1,num+1):
    if num % i == 0:
        print(i)