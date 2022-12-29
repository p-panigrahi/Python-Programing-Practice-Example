# write a program to count number of digits in a numbers
def countNumber(number):
    count = 0
    while (number > 0):
        number = number // 10
        count += 1
    return count
num = int(input("Enter any number"))
result = countNumber(num)
print(result)