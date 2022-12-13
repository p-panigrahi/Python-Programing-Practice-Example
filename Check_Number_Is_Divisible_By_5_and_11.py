# write a program to check number is divisible by 5 and 11
n = int(input("Enter any number : "))
if (n % 5 == 0) and (n % 11 == 0):
    print(f"The Given Number {n} is divisible by 5 and 11")
else:
    print(f"The given number {n} is not divisible by 5 and 11")