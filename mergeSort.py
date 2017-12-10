def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    slice_index = int(len(arr)/2)

    leftArr = mergeSort(arr[:slice_index])
    rightArr = mergeSort(arr[slice_index:])

    i = 0
    j = 0

    finalArr = []

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            finalArr.append(leftArr[i])
            i += 1
        else:
            finalArr.append(rightArr[j])
            j += 1

    if i >= len(leftArr):
        finalArr.extend(rightArr[j:])
    else:
        finalArr.extend(leftArr[i:])

    return finalArr


if __name__ == "__main__":
    arr = input('Input array to be sorted: ')
    arr = [int(x) for x in arr.split()]
    print('Sorted array:', ' '.join(map(str, mergeSort(arr))))
