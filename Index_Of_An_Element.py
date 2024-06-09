def findExtra(a,b,n):
    a2 = set(a)
    b = set(b)
    c = a2.difference(b)
    v = list(c)[0]
    x = a.index(v)
    return x    

a = [4,8,28,40,52,66,91,92]
b = [4,8,40,52,66,91,92]
n = 8

print(findExtra(a,b,n))
