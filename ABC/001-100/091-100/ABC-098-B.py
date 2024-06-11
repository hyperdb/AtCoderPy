# ABC-098 B - Cut and Count
# https://atcoder.jp/contests/abc098/tasks/abc098_b
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = list(getString())

    r = 0
    for i in range(1, len(s)):
        a = set(s[0:i])
        b = set(s[i:])

        c = 0
        for j in a:
            if j in b:
                c += 1
        r = c if c > r else r

    print(r)


if __name__ == "__main__":
    main()
