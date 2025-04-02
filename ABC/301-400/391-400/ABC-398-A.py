# ABC-398 A - Doors in the Center
# https://atcoder.jp/contests/abc398/tasks/abc398_a
#
def getInt():
    return int(input())


def main():
    N = getInt()

    d, m = divmod(N, 2)
    if m == 0:
        print("-" * (d - 1) + "==" + "-" * (d - 1))
    else:
        print("-" * d + "=" + "-" * d)


if __name__ == "__main__":
    main()
