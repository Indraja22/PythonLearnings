def count_evens(nums):
    nums_list = list(nums)
    evens_list = []
    for num in nums_list:
        if num % 2 == 0:
            evens_list.append(num)
    print(len(evens_list))

count_evens([7,8,2,6,4])
