# ABC-303 A - Similar String
# https://atcoder.jp/contests/abc303/tasks/abc303_a
#
def getInt():
    return int(input())


def getStringList():
    return list(input())


def sc(x, y):
    r = False
    if x == y:
        r = True
    elif (x == '1' and y == 'l') or (x == 'l' and y == '1'):
        r = True
    elif (x == '0' and y == 'o') or (x == 'o' and y == '0'):
        r = True
    return r


def main():
    n = getInt()
    s = getStringList()
    t = getStringList()

    u = [0 if sc(s[i], t[i]) else 1 for i in range(n)]

    print('Yes' if sum(u) == 0 else 'No')


if __name__ == "__main__":
    main()
