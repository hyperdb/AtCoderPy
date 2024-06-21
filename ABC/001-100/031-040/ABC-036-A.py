# ABC-036 A - お茶
# https://atcoder.jp/contests/abc036/tasks/abc036_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B = getIntMap()

    print(B // A + (1 if B % A > 0 else 0))


if __name__ == "__main__":
    main()
