def counting_sort(arr):
    max_data = max(arr)
    count_arr = [0] * (max_data + 1)
    for i in range(len(arr)):
        count_arr[arr[i]] = count_arr[arr[i]] + 1

    j = 0
    i = 0

    while i < len(count_arr):
        if count_arr[i] > 0:
            arr[j] = i
            count_arr[i] = count_arr[i] - 1
            j = j + 1
        else:
            i = i + 1


data = [3, 9, 5, 20, 21, 33, 5, 9]

counting_sort(data)

print(data)
