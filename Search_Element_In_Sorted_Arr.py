def searchInSorted(arr, n, k):
    low = 0
    high = n -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == k:
            return 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1