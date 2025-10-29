# ABC-417 B - Search and Delete
# https://atcoder.jp/contests/abc417/tasks/abc417_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, M = getIntMap()
    A = getIntList()
    B = getIntList()

    for b in B:
        if b in A:
            A.remove(b)

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
