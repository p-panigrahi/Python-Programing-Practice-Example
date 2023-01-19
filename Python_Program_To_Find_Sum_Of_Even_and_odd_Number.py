# Python program to find the sum of even and odd number
Number = int(input("Enter any number"))
evenCount = 0
oddCount = 0
for i in range(1,Number+1):
    if i % 2 == 0:
        evenCount += i
    else:
        oddCount += i
print(Number)
print(evenCount)
print(oddCount)