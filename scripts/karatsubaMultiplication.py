from time import perf_counter

def karatsubaMultiply(a, b):

    nA = len(str(abs(a)))
    nB = len(str(abs(b)))

    if nA <= 1 or nB <= 1:
        return a * b

    n = nA if nA > nB else nB

    power = 10**int(n / 2)

    rightA = abs(a) % power
    leftA = int(abs(a) / power)

    rightB = abs(b) % power
    leftB = int(abs(b) / power)

    leftSum = karatsubaMultiply(leftA, leftB)
    rightSum = karatsubaMultiply(rightA, rightB)
    midSum = karatsubaMultiply(leftA + rightA, leftB + rightB) - leftSum - rightSum

    finalresult = int(str(leftSum) + ('0'*n)) + int(str(midSum) + '0'*int(n/2)) + rightSum

    if a < 0 and b < 0 or a > 0 and b > 0:
        return finalresult
    else:
        return -1 * finalresult


if __name__ == "__main__":
    a = int(input('Input integer a: '))
    b = int(input('Input integer b: '))

    start_time = perf_counter()
    print('Karatsuba Multiplication result: %d, takes %f seconds' % (karatsubaMultiply(a, b), perf_counter()-start_time))

    start_time = perf_counter()
    print('Normal multiplication result: %d, takes %f seconds' % (a*b, perf_counter()-start_time))
