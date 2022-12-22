# Write a progran ti find student grade?
sub1 = int(input("Enter First sub1 value : "))
sub2 = int(input("Enter First sub2 value : "))
sub3 = int(input("Enter First sub3 value : "))
sub4 = int(input("Enter First sub4 value : "))
sub5 = int(input("Enter First sub5 value : "))

total = sub1 + sub2 + sub3 + sub4
percentage = (total/500) * 100
print(f"Total Marks {total}")
print(f"Total percentage {percentage}")

if (percentage >= 90):
    print("A Grade")
elif (percentage >= 80):
    print("B Grade")
elif (percentage >= 70):
    print("C Grade")
elif (percentage >= 60):
    print("D Grade")
elif (percentage >= 50):
    print("E Grade")
else:
    print("Fail")
