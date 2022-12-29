# write a program to print fibonacci using function
def fib(number):
    First = 0
    Second = 1
    for i in range(0,number+1):
        if number <= 1:
            Next = number
        else:
            Next = First + Second
            First = Second
            Second = Next
    return Next
num = int(input("Enter any number"))
for i in range(0,num):
    print(fib(i))