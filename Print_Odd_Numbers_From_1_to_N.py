# write a program to find the all odd number between 1 to n
number = int(input("Enter any number"))
for i in range(1,number+1):
    if i % 2 != 0:
        print(f"{i}")