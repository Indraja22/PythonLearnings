def same_first_last(nums):
    return (len(nums) > 1 and (nums[0] == nums[-1])) if True else False
    # if (len(nums) > 1 and (nums[0] == nums[-1])):
    #     return True
    # else:
    #     return False

print(same_first_last([1,2,4,1]))
print(same_first_last([1,2,4]))
print(same_first_last([1,2,1,9]))
