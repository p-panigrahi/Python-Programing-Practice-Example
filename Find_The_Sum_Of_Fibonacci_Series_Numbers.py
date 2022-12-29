# write a program to find the fibonacci series number using loop
num = int(input("Enter any number"))
First = 0
Second = 1
Sum = 0
for i in range(0,num):
    print(First , end="\n")
    Sum += First
    Next = First + Second
    First = Second
    Second = Next
print(Sum)