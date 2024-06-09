arr = [19,12,14,5,67,8,9]
n = 7
k = 67

for i in range(n):
    if arr[i] == k:
        print(arr.index(k)+1)
