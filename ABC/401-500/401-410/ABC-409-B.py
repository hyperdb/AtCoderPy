# ABC-409 B - Citation
# https://atcoder.jp/contests/abc409/tasks/abc409_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()

    x = 100
    while x >= 0:
        c = 0
        for i in A:
            if i >= x:
                c += 1

        if c >= x:
            print(x)
            break

        x -= 1


if __name__ == "__main__":
    main()
