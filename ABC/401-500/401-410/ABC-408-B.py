# ABC-408 B - Compression
# https://atcoder.jp/contests/abc408/tasks/abc408_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    M = getInt()
    A = getIntList()

    C = set()
    for i in A:
        C.add(i)

    C = sorted(C)

    print(len(C))
    print(" ".join(map(str, C)))


if __name__ == "__main__":
    main()
