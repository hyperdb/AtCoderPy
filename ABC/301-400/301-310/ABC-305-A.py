# ABC-305 A - Water Station
# https://atcoder.jp/contests/abc305/tasks/abc305_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    p = n // 5

    print(p * 5 if n % 5 < 3 else (p + 1) * 5)


if __name__ == "__main__":
    main()
