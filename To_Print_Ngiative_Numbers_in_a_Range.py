# write a program to print nagiative number in a range
min = int(input("Enter Min Number : "))
max = int(input("Enter max Number : "))
print(f"All The nagitive Number between {min} to {max}")
for i in range(min,max+1):
    if i < 0:
        print(i,end=" ")