# write a program to read 10 numbers and find their sum and average
sum = 0
print("Enter 10 numbers")
for i in range(1,11):
    num = int(input("Enter any numbers"))
    sum = sum + num
avg = sum / 10
print(f"The sum of 10 numbers {sum}")
print(f"The average of 10 numbers {avg}")