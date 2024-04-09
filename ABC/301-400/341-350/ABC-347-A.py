# ABC-347 A - Divisible
# https://atcoder.jp/contests/abc347/tasks/abc347_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()
    a = getIntList()

    b = [i // k for i in a if i % k == 0]

    print(" ".join(map(str, b)))


if __name__ == "__main__":
    main()
