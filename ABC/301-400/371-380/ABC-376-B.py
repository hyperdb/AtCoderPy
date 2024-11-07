# ABC-376 B - Hands on Ring (Easy)
# https://atcoder.jp/contests/abc376/tasks/abc376_b
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def goR(s, e, n):
    return e - s if e > s else n - abs(e - s)


def goL(s, e, n):
    return n - goR(s, e, n)


def main():
    N, Q = getIntMap()
    HT = getStringListRow(Q)

    L = 1
    R = 2

    d = 0
    for ht in HT:
        h = ht[0]
        t = int(ht[1])

        if h == "R":
            if L < R:
                if L < t < R:
                    d += R - t
                elif R < t:
                    d += t - R
                elif t < L:
                    d += N - R + t
            else:  # R < L
                if R < t < L:
                    d += t - R
                elif L < t:
                    d += R + N - t
                elif t < R:
                    d += R - t
            R = t
        else:
            if L < R:
                if L < t < R:
                    d += t - L
                elif R < t:
                    d += L + N - t
                elif t < L:
                    d += L - t
            else:  # R < L
                if R < t < L:
                    d += L - t
                elif L < t:
                    d += t - L
                elif t < R:
                    d += t + N - L
            L = t

    print(d)


if __name__ == "__main__":
    main()
