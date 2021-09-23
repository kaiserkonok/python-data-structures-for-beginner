def insertion_sort(arr):
    for i in range(len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = current


arr = [3, 2, 39, 32, 301, 392, 304, 220]

insertion_sort(arr)

print(arr)
