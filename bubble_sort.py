def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


data = [3, 9, 2, 25, 12, 9, 3]

bubble_sort(data)

print(data)
