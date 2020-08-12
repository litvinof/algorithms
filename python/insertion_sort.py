def insertion_sort(unsorted_arr):
    for idx in range(1, len(unsorted_arr)):
        # Bubble down the taken element
        sub_idx = idx
        while sub_idx > 0 and unsorted_arr[sub_idx] < unsorted_arr[sub_idx - 1]:
            # Swap
            unsorted_arr[sub_idx], unsorted_arr[sub_idx - 1] = unsorted_arr[sub_idx - 1], unsorted_arr[sub_idx]
            sub_idx -= 1
    return unsorted_arr


test_arr = [4, 3, 7, 193, 1, 6, 2]
print(insertion_sort(test_arr))
