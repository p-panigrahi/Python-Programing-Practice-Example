# write a program to swap to value using arithmatic value
a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
print(f"Before swaping {a} and {b}")
a = a + b
b = a - b
a = a - b
print(f"After swaping {a} and {b}")