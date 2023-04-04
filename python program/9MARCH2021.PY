#coditional stat56ement 
x=int(input("enter the number of a"))
y=int(input("enter the number of b"))
z=x+y
print("x and y sum is",z)
if(z>0):
    print("result number is positive")
    if(z<0):
        print("result  number is negative")
    elif(x>y):
            large=x
            print("a is large then b")
    else:
         large=y
         print("b is large then a")
print("large value is ",large)
