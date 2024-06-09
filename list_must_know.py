lst = [2,4,5,6,7,8,9]
# print(lst[:])
# since list is a mutable object lst2 and lst will have same values
lst2 = lst
# lst2 = lst[:]
lst2.append(100)
print(lst2, lst)
print(lst2[::-1]) # reverse list

def func(n,lst3=[1,2]):
    lst3.append(n)
    return lst3

print(func(6))
print(func(5))
print(func(3))
