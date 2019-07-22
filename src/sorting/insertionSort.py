def insertionSort(arr):
    n = len(arr)
    for j in range(1, n):
        i = j-1
        while i >= 0 and arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i -= 1
    return arr

if __name__ == '__main__':
    arr = input('Input array to be sorted: ')
    arr = [int(x) for x in arr.split()]
    print('Sorted array:', ' '.join(map(str, insertionSort(arr))))
