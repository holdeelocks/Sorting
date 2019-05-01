# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # print(arrA, arrB)
    merged_arr = []
    while (len(arrA) and len(arrB)):
        if (arrA[0] < arrB[0]):
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))

    merged_arr.extend(arrA + arrB)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
        # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[0:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    i = j = 0
    k = start
    for l in range(k, end):
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            arr[l] = left[i]
            i += 1
        else:
            arr[l] = right[j]
            j += 1
    return arr


def merge_sort_in_place(arr, l, r):
    if r - 1 > 1:
        mid = (l + r) // 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)
        merge_in_place(arr, l, mid, r)


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
merge_sort_in_place(arr1, 0, len(arr1) - 1)

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
