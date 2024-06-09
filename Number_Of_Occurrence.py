def count_occ(arr, n, x):
    temp_arr = []
    for i in range(n):
        if arr[i] == x:
            temp_arr.append(x)
    return len(temp_arr)

arr = [19,12,3,45,67,12,12]
c = count_occ(arr, len(arr),19)
print(c)
