def countInversion(arr):

    n = len(arr)
    count = 0

    if n <= 3:
        for i in range(n-1):
            while arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
        return arr, count

    left_arr, count_left = countInversion(arr[:int(n/2)])
    right_arr, count_right = countInversion(arr[int(n/2):])

    final_arr = []

    i, j = 0, 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            final_arr.append(left_arr[i])
            i += 1
        else:
            final_arr.append(right_arr[j])
            j += 1
            count += 1

    if i > len(left_arr):
        final_arr.extend(right_arr[j:])
    else:
        final_arr.extend(left_arr[i:])

    return final_arr, count


if __name__ == "__main__":

    with open('/home/hardianlawi/Downloads/IntegerArray.txt', 'r') as f:
        arr = list(map(int, f.read().split()))

    print(countInversion(arr)[1])
