def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr) - 1
    index = 0
    while True:
        index = (high + low) // 2
        if arr[index] == target:
            return index
        elif arr[index] > target:
            high = index
        elif arr[index] < target:
            low = index

    return -1


print(binary_search([1, 2, 3, 4, 78, 1003, 110002], 3))


def binary_search_recursive(arr, target, low, high):
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1
    if arr[middle] == target:
        return middle
    if arr[middle] > target:
        return binary_search_recursive(arr, target, low, middle)
    elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle, high)
    else:
        return -1
