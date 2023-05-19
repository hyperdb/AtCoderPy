# ABC-121 B - Can you solve this?
# https://atcoder.jp/contests/abc121/tasks/abc121_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m, c = getIntMap()
    b = getIntList()
    a = getIntListRow(n)

    r = 0
    for d in a:
        s = sum([b[i] * d[i] for i in range(m)])
        if s + c > 0:
            r += 1
    print(r)


if __name__ == "__main__":
    main()
