# Python Program to print list items in Reverse order
a = [1,2,3,4,5,6,7,8,9]
print(a[::-1])
a.reverse()
print(a)
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")