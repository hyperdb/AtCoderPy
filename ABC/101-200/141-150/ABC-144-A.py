# ABC-144 A - 9x9
# https://atcoder.jp/contests/abc144/tasks/abc144_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(a * b if a < 10 and b < 10 else -1)


if __name__ == "__main__":
    main()
