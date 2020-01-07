a = float(input("enter value of the first term of the AP: "))
d = float(input("enter mean difference: "))
n = int(input("enter number of terms in the AP: "))
AP = []
sum = 0

for x in range(1,n+1):
    term = a + (x-1)*d
    AP.append(term)
    sum += term
print (AP)

print ("sum of the first ",n," terms of the AP are: ", sum)
