def dSelect(arr, order_statistic):

    n = len(arr)

    if n <= 1:
        return arr[0]

    i = 0

    tmp = sorted(arr[i:i+5])

    C = []

    while (len(tmp) != 0):
        C.append(tmp[int(len(tmp)/2)])
        i += 5
        tmp = sorted(arr[i:i+5])

    P = dSelect(C, int(len(C)/2))

    pivot = arr.index(P)

    arr[0], arr[pivot] = arr[pivot], arr[0]

    i = 1

    for j in range(1, n):
        if arr[0] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i-1], arr[0] = arr[0], arr[i-1]

    pivot = i-1

    if pivot + 1 == order_statistic:
        return arr[pivot]
    elif pivot + 1 > order_statistic:
        return dSelect(arr[:pivot], order_statistic)
    else:
        return dSelect(arr[pivot+1:], order_statistic - pivot - 1)


if __name__ == "__main__":

    print("Input the array:")
    arr = list(map(int, input().split()))
    order_statistic = int(input("Input order statistic:\n"))

    print("")
    print(dSelect(arr, order_statistic))
