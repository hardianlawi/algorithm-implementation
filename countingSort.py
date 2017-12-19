def countingSort(arr, min_num, max_num):
    val_counts = {}
    for i in range(min_num, max_num+1):
        val_counts[i] = 0

    for val in arr:
        val_counts[val] += 1

    output_arr = []
    for key, val in val_counts:
        for i in range(val):
            output_arr.append(key)

    return output_arr

