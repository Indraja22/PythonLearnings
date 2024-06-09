string = "GeeksForGeeks"

dups_list = []
chars_count_dict = {}

for i in string:
    if i not in chars_count_dict:
        chars_count_dict[i] = 1
    else:
        chars_count_dict[i] +=1

for k, v in chars_count_dict.items():
    if v > 1:
        dups_list.append(k)

dups = ",".join(dups_list)
print(dups_list)
print(dups)
