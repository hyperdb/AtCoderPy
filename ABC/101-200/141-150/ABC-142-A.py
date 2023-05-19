# ABC-142 A - Odds of Oddness
# https://atcoder.jp/contests/abc142/tasks/abc142_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    l = n // 2
    m = n % 2

    print(l / n if m == 0 else (l + 1) / n)


if __name__ == "__main__":
    main()
