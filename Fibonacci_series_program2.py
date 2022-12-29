# write a program to print fibonacci series
number = int(input("Enter any number"))
First = 0
Second = 1
for i in range(0,number+1):
    if (number <= 1):
        Next = number
    else:
        Next = First + Second
        First = Second
        Second = Next
    print(Next)