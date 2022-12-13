# write a program to find power of a number
n = int(input("Enter any number"))
e = int(input("Enter any number"))
power = 1
for i in range(1,e+1):
    power = power * n
print(f"The power of {n} and {e} is {power}")