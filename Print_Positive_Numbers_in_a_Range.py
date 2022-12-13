# write a program to print positive number in a range
min = int(input("Enter Min Number : "))
max = int(input("Enter Max Number : "))
print(f"The Positive number between {min} to {max}")
for i in range(min,max+1):
    if i >= 0:
        print(i , end=" ")