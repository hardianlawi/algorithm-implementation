from random import randrange

def rSelect(arr, order_statistic):
    n = len(arr)

    if n == 1:
        return arr[0]

    pivot = randrange(n)

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
        return rSelect(arr[:pivot], order_statistic)
    else:
        return rSelect(arr[pivot+1:], order_statistic - pivot - 1)


if __name__ == "__main__":

    print("Input the array:")
    arr = list(map(int, input().split()))
    order_statistic = int(input("Input order statistic:\n"))

    print("")
    print(rSelect(arr, order_statistic))
