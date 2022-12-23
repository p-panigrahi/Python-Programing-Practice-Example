# write aprogram to find the sum and average of N natural numbers
number = int(input("Enter any number"))
total = 0
for i in range(1,number+1):
    total = total + i
avg = total / number
print(f"The sum of N Natural number is {total}")
print(f"The avg of N natural number is {avg}")