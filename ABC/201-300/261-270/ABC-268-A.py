# ABC-268 A - Five Integers
# https://atcoder.jp/contests/abc268/tasks/abc268_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    n = getIntList()

    print(len(list(set(n))))


if __name__ == "__main__":
    main()
