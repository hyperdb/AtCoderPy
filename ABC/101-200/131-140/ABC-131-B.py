# ABC-131 B - Bite Eating
# https://atcoder.jp/contests/abc131/tasks/abc131_b
#
def getIntMap():
    return map(int, input().split())


def main():
    n, l = getIntMap()

    a = [i + l for i in range(n)]
    s = sum(a)

    if min(a) >= 0:
        m = min(a)
    elif max(a) < 0:
        m = max(a)
    else:
        b = min([i for i in a if i >= 0])
        c = max([i for i in a if i < 0])

        m = b if abs(c) >= b else c

    print(s - m)


if __name__ == "__main__":
    main()
