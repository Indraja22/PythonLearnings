def merge_dictionary(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {"a":1,"b":2,"c":3}
dict2 = {"d":4,"e":5,"f":6}
print(merge_dictionary(dict1,dict2))
print(dict2)

res = {**dict1, **dict2}
print(res)
