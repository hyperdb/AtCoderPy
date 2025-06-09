# ABC-408 A - Timeout
# https://atcoder.jp/contests/abc408/tasks/abc408_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, S = getIntMap()
    T = getIntList()

    prev = 0
    result = True
    for i in T:
        diff = i - prev
        if diff > S:
            result = False
            break
        prev = i

    print("Yes" if result else "No")


if __name__ == "__main__":
    main()
