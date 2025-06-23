# ABC-410 B - Reverse Proxy
# https://atcoder.jp/contests/abc410/tasks/abc410_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, Q = getIntMap()
    X = [999] + getIntList()

    B = [999] + [0] * N
    A = []

    for i in range(Q):
        j = X[i + 1]
        if j == 0:
            k = min(B)
            j = B.index(k)
        B[j] += 1
        A.append(j)

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
