# ABC-361 A - Insert
# https://atcoder.jp/contests/abc361/tasks/abc361_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, K, X = getIntMap()
    A = getIntList()

    b = A[:K] + [X] + A[K:]
    print(" ".join(map(str, b)))


if __name__ == "__main__":
    main()
