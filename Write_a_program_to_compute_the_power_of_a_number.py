# write a program to compute the power of a number
base = 3
exponent = 5
result = 1
for i in range(exponent,0,-1):
    result *= base
print(result)