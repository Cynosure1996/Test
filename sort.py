def insert_sort(arr, left = 0, right = None):
    if (right == None):
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while (j >= left and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return 1



def timsort(arr):
    min_area = 32
    n = len(arr)
    for i in range(0,n, min_area):
        insert_sort(arr, i, min((i + min_area - 1), (n-1)))

    size = min_area
    while (size < n):
        for s in range(0, n, size * 2):
            mid = s + size - 1
            end = min((s + size * 2 - 1), (n - 1))
            merged = merge(left = arr[s:mid + 1], right = arr[mid + 1: end + 1])
            arr[s:s+len(merged)]= merged
    size *= 2
    return arr
l1 = [34,10,64,51,32,21]
res = timsort(l1)
print(res)