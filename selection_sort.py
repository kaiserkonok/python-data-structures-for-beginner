def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr) - 1):
            if arr[min_index] > arr[j]:
                min_index = j

        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp


data = [3, 9, 1, 2, 9, 8, 5, 6, 10]

selection_sort(data)

print(data)
