# write a program to find the prime factor of a number
Number = int(input("Enter any positive number"))
for i in range(2,Number+1):
    if (Number % i == 0):
        isPrime = 1
        for j in range(2,(i//2+1)):
            if (i % j == 0):
                isPrime = 0
                break
        if isPrime == 1:
            print(f"{i} is prime factor of given {Number}")