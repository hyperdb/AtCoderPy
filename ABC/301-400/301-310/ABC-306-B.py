# ABC-306 B - Base 2
# https://atcoder.jp/contests/abc306/tasks/abc306_b
#
def getIntList():
    return list(map(int, input().split()))


def main():
    a = getIntList()

    r = 0
    for i in range(len(a)):
        if a[i] == 0:
            continue
        r += (2 ** i)

    print(r)


if __name__ == "__main__":
    main()
