my_list = [3,4,5,3,1,4,4,5,7,8,9,10,11,10]
my_dict = {}
dups_list = []
count = 0
for i in my_list:
    if i in my_dict:
        count = my_dict[i] + 1
        my_dict[i] = count
    else:
        my_dict[i] = 1

for i, v in my_dict.items():
    if(v > 1):
        dups_list.append(i)

print(dups_list)

