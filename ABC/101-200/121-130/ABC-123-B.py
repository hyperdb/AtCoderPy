# ABC-123 B - Five Dishes
# https://atcoder.jp/contests/abc123/tasks/abc123_b
#
def getIntRow(N):
    return [int(input()) for _ in range(N)]


def dec(n):
    m = n % 10
    return m if m == 0 else 10 - m


def main():
    x = getIntRow(5)
    y = [[dec(x[i]), x[i]] for i in range(len(x))]

    y.sort()
    y.reverse()

    s = 0
    for i in range(len(y)):
        s += y[i][1] if i == 0 else sum(y[i])
    print(s)


if __name__ == "__main__":
    main()
