def binary_search(arr, find):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == find:
            return mid
        elif arr[mid] < find:
            left = mid + 1
        else:
            right = mid - 1

    return False


data = [1, 2, 3]

search = binary_search(data, 3)

if search:
    print("Data found at index =>", search)
else:
    print("Data not found!!")
