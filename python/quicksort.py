# Worst case: O(n^2)
# Average case: O(log(n))


def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    pivot = arr.pop()
    greater_arr = []
    lower_arr = []

    for i in arr:
        if i > pivot:
            greater_arr.append(i)
        else:
            lower_arr.append(i)

    return quick_sort(lower_arr) + [pivot] + quick_sort(greater_arr)


test_arr = [4, 3, 7, 193, 1, 6, 2]
print(quick_sort(test_arr))
