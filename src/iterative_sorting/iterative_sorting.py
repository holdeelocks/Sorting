# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        curr_idx = i
        smallest_idx = curr_idx
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(curr_idx, len(arr)):
            if arr[j] < arr[smallest_idx]:
                smallest_idx = j

        # TO-DO: swap
        temp = arr[curr_idx]
        arr[curr_idx] = arr[smallest_idx]
        arr[smallest_idx] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True

    while (swapped):
        count = 0
        for i in range(0, len(arr) - 1):
            first = arr[i]
            second = arr[i + 1]
            if second < first:
                arr[i] = second
                arr[i + 1] = first
                count += 1

        if count == 0:
            swapped = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
