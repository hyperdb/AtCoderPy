# ABC-168 B - ... (Triple Dots)
# https://atcoder.jp/contests/abc168/tasks/abc168_b
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    k = getInt()
    s = getString()

    print(s[:k] + ('...' if len(s) > k else ''))


if __name__ == "__main__":
    main()
