# ABC-034 B - ペア
# https://atcoder.jp/contests/abc034/tasks/abc034_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print(n + (1 if n % 2 == 1 else -1))


if __name__ == "__main__":
    main()
