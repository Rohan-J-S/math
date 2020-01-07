first = float(input("enter value of coefficient of x in eq 1: "))
second = float(input("enter value of coefficient of y in eq 1: "))
rhs1 = float(input("enter rhs value of equation1: "))
third = float(input("enter value of coefficient of x in eq 2: "))
fourth = float(input("enter value of coefficient of y in eq 2: "))
rhs2 = float(input("enter rhs value of equation2: "))

y1 = second * third
y2 = fourth * first
y3 = (rhs1*third)-(rhs2*first)
y = y3/(y1-y2)

x = (rhs1-(y*second))/first
print ("the value of x is: ", x)
print ("the value of y is: ", y)
