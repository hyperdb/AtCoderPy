# ABC-366 A - Election 2
# https://atcoder.jp/contests/abc366/tasks/abc366_a
#
def getIntMap():
    return map(int, input().split())


def main():
    N, T, A = getIntMap()

    print("No" if T <= N // 2 and A <= N // 2 else "Yes")


if __name__ == "__main__":
    main()
