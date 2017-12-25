def squareRoot(x):
    start = 1
    end = x

    while (abs(x - start*start) > 0.000000001):
        mid = (start+end)/2
        if (mid * mid < x):
            start = mid
        else:
            end = mid

    return start


if __name__ == '__main__':
    x = int(input("Find square root of: "))
    print(squareRoot(x))
