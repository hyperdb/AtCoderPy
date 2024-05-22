# ABC-351 A - The bottom of the ninth
# https://atcoder.jp/contests/abc351/tasks/abc351_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    a = getIntList()
    b = getIntList()

    print(sum(a) - sum(b) + 1)


if __name__ == "__main__":
    main()
