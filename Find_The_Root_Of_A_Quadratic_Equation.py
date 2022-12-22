# write a program to find the roots of a Quadratic equation?
import math
a = int(input("Enter a value of Quadratic equation"))
b = int(input("Enter b value of Quadratic Equation"))
c = int(input("Enter c value of Quadratic Equation"))
discrimant = (b*b)-(4*a*c)
if(discrimant > 0):
    root1 = (-b+math.sqrt(discrimant)/(2*a))
    root2 = (-b-math.sqrt(discrimant)/(2*a))
    print("Two Distinct real roots exist : root1 =%.2f and root2 = %.2f"%(root1,root2))
elif (discrimant == 0):
    root1 = root2 = -b/(2*a)
    print("Two equal and real roots Exixts : root1 = %.2f and root2 = %.2f"%(root1,root2))
elif (discrimant < 0):
    root1 = root2 = -b/(2*a)
    imaginary = math.sqrt(-discrimant)/(2*a)
    print("Two Distinct comple roots exists : root1 = %.2f+%.2f and root2 = %.2f-%.2f"%(root1,imaginary,root2,imaginary))