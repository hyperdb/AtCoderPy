# ABC-183 A - ReLU
# https://atcoder.jp/contests/abc183/tasks/abc183_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print(n if n >= 0 else 0)


if __name__ == "__main__":
    main()
