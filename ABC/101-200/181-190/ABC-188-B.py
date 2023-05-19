# ABC-188 B - Orthogonality
# https://atcoder.jp/contests/abc188/tasks/abc188_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()
    b = getIntList()

    c = []
    for i in range(n):
        c.append(a[i] * b[i])

    print('Yes' if sum(c) == 0 else 'No')


if __name__ == "__main__":
    main()
