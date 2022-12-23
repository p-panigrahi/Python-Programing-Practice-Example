# write a program to find distance between two points
import math
x1 = int(input("Enter the first point coordinate"))
y1 = int(input("Enter the first point coordinate"))
x2 = int(input("Enter the second point coordinate"))
y2 = int(input("Enter the second point coordinate"))
x = math.pow((x2 - x1),2)
y = math.pow((y2 -y1),2)
print(x)
print(y)
print(math.sqrt(x+y))
distance = math.sqrt(x+y)
print(f"The distance between two points {distance}")