
a = 2
b = 1
for x in range(1,52):
    l = []
    for y in range(b,a):
        l += [y]
    b = a
    a += x
    
s = 0
for z in l:
    s += z
print(s)
print(l)
