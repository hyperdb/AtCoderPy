#
#
#
def getIntMap():
    return map(int, input().split())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    N, K = getIntMap()
    s = getIntRow(N)

    if 0 in s:
        print(N)
    else:
        r = 0
        p = 1
        c = 0
        for l in range(N):
            while r < N and p * s[r] <= K:
                p *= s[r]
                r += 1
            c = max(c, r - l)
            if l == r:
                r += 1
            else:
                p //= s[l]
        print(c)


if __name__ == "__main__":
    main()
