x5 = int(input("enter coeffecient of x**5: "))
x4 = int(input("enter coeffecient of x**4: "))
x3 = int(input("enter coeffecient of x**3: "))
x2 = int(input("enter coeffecient of x**2: "))
x1 = int(input("enter coeffecient of x**1: "))
cons = int(input("enter constant value to make the equation equal to 0: "))
zeros = []

for x in range(-cons,cons+1):

    zero = ((x**5)*x5)+((x**4)*x4)+((x**3)*x3)+((x**2)*x2)+((x**1)*x1)+cons
    if zero == 0:
        zeros.append(x)
    
print ("integer zeros of the equation are: ", zeros)
