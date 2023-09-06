# ABC-300 A - N-choice question
# https://atcoder.jp/contests/abc300/tasks/abc300_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, a, b = getIntMap()
    c = [0] + getIntList()

    print(c.index(a + b))


if __name__ == "__main__":
    main()
