# ABC-162 A - Lucky 7
# https://atcoder.jp/contests/abc162/tasks/abc162_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print('Yes' if '7' in list(str(n)) else 'No')


if __name__ == "__main__":
    main()
