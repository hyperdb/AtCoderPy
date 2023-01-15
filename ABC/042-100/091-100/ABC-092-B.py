# ABC-092 B - Chocolate
# https://atcoder.jp/contests/abc092/tasks/abc092_b
#
def getInt():
    return int(input())


def getIntMap():
    return map(int, input().split())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    n = getInt()
    d, x = getIntMap()
    a = getIntRow(n)

    c = 0
    for i in range(n):
        for j in range(d + 1):
            if j * a[i] + 1 <= d:
                c += 1
    print(x + c)


if __name__ == "__main__":
    main()
