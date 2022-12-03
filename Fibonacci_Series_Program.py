# write a program to find fibonacci program using for loop
num = int(input("Enter the range of number"))
first_value = 0
second_value = 1
for i in range(0,num):
    if i <= 1 :
        Next = i
    else:
        Next = first_value + second_value
        first_value = second_value
        second_value = Next
    print(Next)