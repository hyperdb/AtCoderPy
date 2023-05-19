# ABC-102 A - Multiple of 2 and N
# https://atcoder.jp/contests/abc102/tasks/abc102_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print(n if n % 2 == 0 else n * 2)


if __name__ == "__main__":
    main()
