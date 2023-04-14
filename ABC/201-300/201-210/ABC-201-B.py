# ABC-201 B - Do you know the second highest mountain?
# https://atcoder.jp/contests/abc201/tasks/abc201_b
#
def getInt():
    return int(input())


def getStringListRow(N):
    return [list(input().split()) for _ in range(N)]


def main():
    n = getInt()
    x = getStringListRow(n)

    y = dict()
    z = []
    for s, t in x:
        y[t] = s
        z.append(int(t))
    z.sort()
    z.reverse()

    print(y[str(z[1])])


if __name__ == "__main__":
    main()
