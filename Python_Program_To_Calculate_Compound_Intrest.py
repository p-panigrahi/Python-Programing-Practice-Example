# write a python program to find the compound intrest
P = float(input("Enter Principal"))
T = int(input("Enter Time Period"))
R = float(input("Enter Rate of intrest"))
a = P *(1+(R/100))**T
ci = a-P
print(ci)