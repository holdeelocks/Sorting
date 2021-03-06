def merge(arrA, arrB):
    merged_arr = []
    while (len(arrA) and len(arrB)):
        if (arrA[0] < arrB[0]):
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))

    merged_arr.extend(arrA + arrB)

    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[0:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


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
        midpt = (l + r) // 2
        merge_sort_in_place(arr, l, midpt)
        merge_sort_in_place(arr, midpt, r)
        merge_in_place(arr, l, midpt, r)


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
merge_sort_in_place(arr1, 0, len(arr1) - 1)

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
