# write a program to check a comon letters in two string
a = input("Enter First String")
b = input("Enter Second String")
c = set(a) and set(b)
for i in c:
    print(i)