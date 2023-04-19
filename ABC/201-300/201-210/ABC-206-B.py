# ABC-206 B - Savings
# https://atcoder.jp/contests/abc206/tasks/abc206_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    s = 1
    c = 1
    while s < n:
        c += 1
        s += c
    print(c)


if __name__ == "__main__":
    main()
