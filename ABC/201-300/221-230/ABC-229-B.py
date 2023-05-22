# ABC-229 B - Hard Calculation
# https://atcoder.jp/contests/abc229/tasks/abc229_b
#
def getStringMap():
    return input().split()


def main():
    a, b = getStringMap()

    l = max(len(a), len(b))
    if len(a) != len(b):
        a = a.zfill(l)
        b = b.zfill(l)

    r = 'Easy'
    for i in range(l):
        if int(a[i]) + int(b[i]) > 9:
            r = 'Hard'
            break
    print(r)


if __name__ == "__main__":
    main()
