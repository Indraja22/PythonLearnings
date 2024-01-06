def has23(nums):
    if((nums[0] in (2,3)) or (nums[1] in (2,3))):
        return True
    else:
        return False
        
print(has23([4,2]))
print(has23([5,3]))
print(has23([4,1]))
