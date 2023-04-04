i=1
while(i<=7):
    a=input("Enter student name :")
    english = float(input(" Please enter English Marks: "))
    math = float(input(" Please enter Math score: "))
    computers = float(input(" Please enter Computer Marks: "))
    physics = float(input(" Please enter Physics Marks: "))
    chemistry = float(input(" Please enter Chemistry Marks: "))
    total = english + math + computers + physics + chemistry
    percentage = (total / 500) * 100
    print(a,"percentage is",percentage)
    if(percentage >= 70):
        print("First division  and", a ,"got Grade A")
        print(a ," is PASS")
    elif(percentage >= 50):
        print("Second division  and", a ,"got Grade B")
        print(a ," is PASS")
    elif(percentage >= 35):
        print("Third division  and", a ,"got Grade C")
        print(a ," is PASS")
    else:
            print(a ," is FAIL")
    i+=1