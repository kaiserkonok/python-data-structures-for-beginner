def insertion_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp


data = [3, 9, 2, 20, 13, 30, 50, 31, 90]

insertion_sort(data)

print(data)
