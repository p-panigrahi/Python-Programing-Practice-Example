# write a program to print even number from 1 to N
number = int(input("Enter Any number"))
for i in range(1,number+1):
    if i % 2 == 0:
        print(f"{i}")