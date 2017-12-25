"""Strassen Algorithm."""
import numpy as np


def strassen_algorithm(x, y):
    """Return nxn Matrix multiplication."""
    if x.size == 1 or y.size == 1:
        return x * y

    n = x.shape[0]

    if n % 2 == 1:
        x = np.pad(x, (0, 1), mode='constant')
        y = np.pad(y, (0, 1), mode='constant')

    m = int(np.ceil(n / 2))

    # Split matrix x
    a = x[: m, : m]
    b = x[: m, m:]
    c = x[m:, : m]
    d = x[m:, m:]

    # Split matrix y
    e = y[: m, : m]
    f = y[: m, m:]
    g = y[m:, : m]
    h = y[m:, m:]

    # Calculate the seven products of matrices
    p1 = strassen_algorithm(a, f - h)
    p2 = strassen_algorithm(a + b, h)
    p3 = strassen_algorithm(c + d, e)
    p4 = strassen_algorithm(d, g - e)
    p5 = strassen_algorithm(a + d, e + h)
    p6 = strassen_algorithm(b - d, g + h)
    p7 = strassen_algorithm(a - c, e + f)

    # Initialize matrix to store results
    result = np.zeros((2 * m, 2 * m), dtype=np.int32)

    # Calculate each quadrant inside matrix
    result[: m, : m] = p5 + p4 - p2 + p6
    result[: m, m:] = p1 + p2
    result[m:, : m] = p3 + p4
    result[m:, m:] = p1 + p5 - p3 - p7

    return result[: n, : n]

if __name__ == "__main__":
    print("Please input matrix X:")
    x = []
    tmp = input().split()
    while len(tmp) != 0:
        x.append(tmp)
        tmp = input().split()

    print("Please input matrix Y:")
    y = []
    tmp = input().split()
    while len(tmp) != 0:
        y.append(tmp)
        tmp = input().split()

    x = np.array(x, dtype=np.float32)
    y = np.array(y, dtype=np.float32)

    assert x.size == y.size, "two matrices have to be of size nxn"

    print('Matrix multiplication result: ')
    print(strassen_algorithm(x, y))

    print(np.matmul(x, y))
