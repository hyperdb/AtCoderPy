# ABC-301 A - Overall Winner
# https://atcoder.jp/contests/abc301/tasks/abc301_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    if s.count('A') > s.count('T'):
        print('A')
    elif s.count('A') < s.count('T'):
        print('T')
    elif s.rfind('A') < s.rfind('T'):
        print('A')
    else:
        print('T')


if __name__ == "__main__":
    main()
