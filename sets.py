def example():
    new1 = set()
    print(type(new1))
    print(new1)
    new_3 = {7, 9, 10, 11, 12}
    new2 = {8, 9, 14, 11, 15}
    print(new_3 & new2) #intersection
    print(new_3 | new2) #union
    print(new_3 - new2) #difference

    print(8 in new2)
    print(18 in new2)
    for i in new2:
        print(i)

example()    