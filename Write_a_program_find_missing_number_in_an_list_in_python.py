# write a program to find the missing number in a list
newList = [1,2,3,4,6,7]
a = 0
sum = 0
c = 0
for i in newList:
    a = i*(i+1)/2
    sum = sum+i
    c = a-sum
print(a)
print(sum)
print(int(c))
