ints_list = [4, 3, 2, 1]

sorted_list = sorted(ints_list)

expected_list = list(range(0,len(ints_list)+1))
print(expected_list)
ints = set(expected_list) - set(ints_list)
print(list(ints)[0])
    