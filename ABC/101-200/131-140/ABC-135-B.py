# ABC-135 B - 0 or 1 Swap
# https://atcoder.jp/contests/abc135/tasks/abc135_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    p = getIntList()

    s = p.copy()
    s.sort()

    c = 0
    for i in range(len(p)):
        if p[i] != s[i]:
            c += 1
    print('YES' if c in [0, 2] else 'NO')


if __name__ == "__main__":
    main()
