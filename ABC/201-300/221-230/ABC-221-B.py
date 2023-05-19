# ABC-221 B - typo
# https://atcoder.jp/contests/abc221/tasks/abc221_b
#
def getString():
    return input()


def main():
    s = list(getString())
    t = list(getString())
    x = []
    y = []

    for i in range(len(s) - 1):
        if s[i] != t[i]:
            x.append(s[i])
            x.append(s[i + 1])
            y.append(t[i])
            y.append(t[i + 1])
            break

    y.reverse()
    if len(x) == 0 or x == y:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
