# ABC-281 A - Count Down
# https://atcoder.jp/contests/abc281/tasks/abc281_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    while n >= 0:
        print(n)
        n -= 1


if __name__ == "__main__":
    main()
