def search_element_in_array(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

arr=[9,10,3,4,56,12]
n = 6
x = 12
s = search_element_in_array(arr, n, x)
print(s)
