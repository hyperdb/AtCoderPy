# ABC-115 A - Christmas Eve Eve Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_a
#
def getInt():
    return int(input())


def main():
    d = getInt()

    w = ['Christmas']
    for i in range(25 - d):
        w.append('Eve')
    print(' '.join(w))


if __name__ == "__main__":
    main()
