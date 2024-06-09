salaries_list = [60000,80000,120000,70000]
# n = 2
# sorted_salaries_list = sorted(salaries_list)
# input_list = []
# print(sorted_salaries_list)

# for i in range(0,n):
#     input_list.append(sorted_salaries_list[i])
# inequity = max(input_list) - min(input_list)   

# print(inequity)

def min_inequity(salaries, n):
    sorted_salaries = sorted(salaries)
    input_list = []
    for i in range(0,n):
        input_list.append(sorted_salaries[i])
    inequity = max(input_list) - min(input_list)
    return inequity    

print(min_inequity(salaries_list,3))