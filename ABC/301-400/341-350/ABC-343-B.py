# ABC-343 B - Adjacency Matrix
# https://atcoder.jp/contests/abc343/tasks/abc343_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    a = getIntListRow(n)

    for j in range(n):
        k = []
        for i in range(n):
            if a[j][i] == 1:
                k.append(i + 1)
        print(" ".join(map(str, k)))


if __name__ == "__main__":
    main()
