# ABC-194 B - Job Assignment
# https://atcoder.jp/contests/abc194/tasks/abc194_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    l = getIntListRow(n)

    a = [i for i, j in l]
    b = [j for i, j in l]

    t = max(a) + max(b)
    for i in range(n):
        for j in range(n):
            if i == j:
                w = a[i] + b[j]
            else:
                w = max(a[i], b[j])
            t = min(t, w)
    print(t)


if __name__ == "__main__":
    main()
