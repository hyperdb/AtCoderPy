# ABC-156 A - Beginner
# https://atcoder.jp/contests/abc156/tasks/abc156_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, r = getIntMap()

    print(r + (0 if n >= 10 else 100 * (10 - n)))


if __name__ == "__main__":
    main()
