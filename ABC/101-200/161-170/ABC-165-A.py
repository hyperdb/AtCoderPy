# ABC-165 A - We Love Golf
# https://atcoder.jp/contests/abc165/tasks/abc165_a
#
def getInt():
    return int(input())


def getIntMap():
    return map(int, input().split())


def main():
    k = getInt()
    a, b = getIntMap()

    f = False
    for i in range(a, b + 1):
        if i % k == 0:
            f = True
            break
    print('OK' if f else 'NG')


if __name__ == "__main__":
    main()
