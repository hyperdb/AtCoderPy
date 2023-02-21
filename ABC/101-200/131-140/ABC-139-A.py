# ABC-139 A - Tenki
# https://atcoder.jp/contests/abc139/tasks/abc139_a
#
def getString():
    return input()


def main():
    s = list(getString())
    t = list(getString())

    c = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
