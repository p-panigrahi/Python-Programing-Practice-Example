#write a program to find the sum of 10 numbers and skip negative numbers
sum = 0
for i in range(1,11):
    num = int(input("Enter any number"))
    if num < 0:
        continue
    sum = sum + num
print(f"The sum of 10 numbers by skipping negitave numbers is {sum}")