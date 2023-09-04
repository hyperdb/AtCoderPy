# ABC-298 A - Job Interview
# https://atcoder.jp/contests/abc298/tasks/abc298_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    print('Yes' if s.count('o') > 0 and s.count('x') == 0 else 'No')


if __name__ == "__main__":
    main()
