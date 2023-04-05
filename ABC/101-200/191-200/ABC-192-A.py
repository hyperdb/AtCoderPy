# ABC-192 A - Star
# https://atcoder.jp/contests/abc192/tasks/abc192_a
#
def getInt():
    return int(input())


def main():
    x = getInt()

    y = x % 100

    print(100 if y == 0 else 100 - y)


if __name__ == "__main__":
    main()
