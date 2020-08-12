def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2

        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])

        arr = merge(left, right)

    return arr


def merge(left, right):
    arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr.extend(left[i:])
    arr.extend(right[j:])

    return arr


test_arr = [4, 3, 7, 193, 1, 6, 2]
merge_sort(test_arr)
print(merge_sort(test_arr))
