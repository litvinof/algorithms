def selection_sort(unsorted_arr):
    for idx in range(len(unsorted_arr)):
        # Find minimum
        minimum = idx
        for sub_idx in range(idx + 1, len(unsorted_arr)):
            if unsorted_arr[minimum] > unsorted_arr[sub_idx]:
                minimum = sub_idx

        # Swap
        unsorted_arr[idx], unsorted_arr[minimum] = unsorted_arr[minimum], unsorted_arr[idx]

    return unsorted_arr


test_arr = [4, 3, 7, 193, 1, 6, 2]
print(selection_sort(test_arr))
