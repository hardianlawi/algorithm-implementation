import numpy as np


def distance(v1, v2):
    dx = v1[0] - v2[0]
    dy = v1[1] - v2[1]
    return np.linalg.norm([dx, dy])

def closestSplitPair(Px, Py, d):

    xbar = Px[int(len(Px)/2)-1][0]
    Sy = [tup for tup in Py if abs(tup[0] - xbar) < d]

    best_d = None
    for i in range(len(Sy)-1):
        for j in range(1, min(8, len(Sy)-i)):
            tmp = distance(Sy[i], Sy[i+j])
            if best_d is None or best_d > tmp:
                best_d = tmp

    return best_d

def closestPairs(P):

    if len(P) <= 3:
        d = None
        for i in range(len(P)):
            for j in range(i+1, len(P)):
                tmp = distance(P[i], P[j])
                if d is None or d > tmp:
                    d = tmp
        return d

    Px = sorted(P, key=lambda x: x[0])
    Py = sorted(P, key=lambda y: y[1])

    Px_left = Px[:int(len(Px)/2)]
    Px_right = Px[int(len(Px)/2):]

    d_left = closestPairs(Px_left)
    d_right = closestPairs(Px_right)
    d = min(d_left, d_right)

    d_split = closestSplitPair(Px, Py, d)

    return min(d_split, d) if d_split is not None else d

if __name__ == '__main__':

    P = []
    print("Input x y pairs:")
    tmp = input().split()
    while len(tmp) != 0:
        if len(P) != 0 and len(tmp) != len(P[-1]):
            print("Number of coords has to be the same as the others")
            tmp = input().split()
            continue
        P.append(list(map(float, tmp)))
        tmp = input().split()

    print("Closest pairs: ", closestPairs(P))
