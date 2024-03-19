# ABC-340 B - Append
# https://atcoder.jp/contests/abc340/tasks/abc340_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    q = getIntListRow(n)

    buf = []

    for i, j in q:
        if i == 1:
            buf.append(j)
        else:
            print(buf[j * -1])


if __name__ == "__main__":
    main()
