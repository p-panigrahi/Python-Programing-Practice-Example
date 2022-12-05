# write a program to find the factors of number
value = int(input("Enter any number"))
print(f'Result of given number{value}')
for i in range(1,value+1):
    if value % i == 0:
        print(i)