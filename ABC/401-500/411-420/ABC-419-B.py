# ABC-419 B - Get Min
# https://atcoder.jp/contests/abc419/tasks/abc419_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    Q = getInt()

    b = []
    for _ in range(Q):
        q = getIntList()
        if q[0] == 1:
            b.append(q[1])
        else:
            x = min(b)
            i = b.index(x)
            b.pop(i)
            print(x)


if __name__ == "__main__":
    main()
