# ABC-340 C - Divide and Divide
# https://atcoder.jp/contests/abc340/tasks/abc340_c
#
def getInt():
    return int(input())


def divide(n):
    return [n // 2, (n + 1) // 2]


def main():
    n = getInt()

    d = dict()
    d.setdefault(n, 1)

    p = 0
    while len(d) > 0:
        k = max(d.keys())

        v = d[k]

        p += (k * v)
        d.pop(k)

        for x in divide(k):
            if x == 1:
                continue
            else:
                d.setdefault(x, 0)
                d[x] += v

    print(p)


if __name__ == "__main__":
    main()
