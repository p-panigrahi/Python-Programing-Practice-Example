#            *
#          * *
#        * * *
#      * * * *
#    * * * * *

for r in range(1,6):
    for c in range(5,0,-1):
        if c<=r:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
