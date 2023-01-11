# ABC-084 B - Postal Code
# https://atcoder.jp/contests/abc084/tasks/abc084_b
#
def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def check(s, a, b):
    s = s.split('-')
    if len(s) != 2:
        return False
    if len(s[0]) == a and len(s[1]) == b:
        return True
    return False


def main():
    a, b = getIntMap()
    s = getString()

    print('Yes' if check(s, a, b) else 'No')


if __name__ == "__main__":
    main()
