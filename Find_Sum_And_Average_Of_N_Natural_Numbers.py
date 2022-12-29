# write a program to find the sum and avg of N natural numbers
sum = 0
num = int(input("Enter any number"))
for i in range(1,num+1):
    sum += i
    avg = sum / i
print(sum)
print(avg)