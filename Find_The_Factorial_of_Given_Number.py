# write a program find the factorial of given number
num = int(input("Enter any numbar : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
    print(f"{fact}")