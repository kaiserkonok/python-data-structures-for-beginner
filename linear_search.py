def linear_search(arr, find):
    for i in range(len(arr)):
        if arr[i] == find:
            return i

    return False


data = [1, 2, 3]

find = linear_search(data, 3)

if find:
    print("Data found at index =>", find)
else:
    print("Data not found!!")
