# ABC-299 A - Treasure Chest
# https://atcoder.jp/contests/abc299/tasks/abc299_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    print('in' if s.find('|') < s.find('*') < s.rfind('|') else 'out')


if __name__ == "__main__":
    main()
