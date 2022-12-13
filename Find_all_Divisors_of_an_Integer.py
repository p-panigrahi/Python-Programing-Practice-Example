# write a program to find all divisors of an integer
num = int(input("Enter any integer to find divisors : "))
print("The Divisors of the number : ")
for i in range(1,num+1):
    if num % i == 0:
        print(i)