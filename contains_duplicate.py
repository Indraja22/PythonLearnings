input_list = [1,3,5,7]
new_list = []
dups_list = []

for i in input_list:
    if i not in new_list:
        new_list.append(i)
    else:
        dups_list.append(i)
if len(dups_list) > 0:
    print("True")
else:
    print("False")
    