# Python program to find the sum and avg of n natural number
# Number = int(input("Enter any number"))
# sum = 0
# avg = 0
# for i in range(1,Number+1):
#     sum += i
#     avg = sum/Number
# print(Number)
# print(sum)
# print(avg)

# Method 2 Using Function
def Number(num):
    sum = 0
    avg = 0
    for i in range(1,num+1):
        sum += i
        avg = sum/num
    return sum , avg
num = int(input("Enter any number"))
Result = Number(num)
print(Result)
