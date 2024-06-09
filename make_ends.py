def make_ends(nums):
    new_nums_arr = []
    new_nums_arr.append(nums[0])
    new_nums_arr.append(nums[-1])
    return new_nums_arr

print(make_ends([6,2,9,10]))
print(make_ends([2,9,1]))
print(make_ends([8,2,5]))
