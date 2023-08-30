# ABC-295 A - Probably English
# https://atcoder.jp/contests/abc295/tasks/abc295_a
#
def getInt():
    return int(input())


def getStringList():
    return list(input().split())


def main():
    n = getInt()
    w = getStringList()
    d = ['and', 'not', 'that', 'the', 'you']

    w.sort()

    r = False
    for x in set(w):
        if x in d:
            r = True
            break

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
