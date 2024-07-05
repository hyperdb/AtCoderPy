# ABC-009 A - 引越し作業
# https://atcoder.jp/contests/abc009/tasks/abc009_1
#
def getInt():
    return int(input())


def main():
    N = getInt()
    d, m = divmod(N, 2)

    print(d + m)


if __name__ == "__main__":
    main()
