# ABC-065 B - Trained?
# https://atcoder.jp/contests/abc065/tasks/abc065_b
#
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    n = getInt()
    a = getIntRow(n)

    a.insert(0, 0)
    b = 1
    c = 0
    f = False
    for i in range(n):
        c += 1
        b = a[b]
        if b == 2:
            f = True
            break
    print(c if f else -1)


if __name__ == "__main__":
    main()
