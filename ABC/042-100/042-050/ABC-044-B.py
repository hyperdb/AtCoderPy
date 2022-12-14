# ABC-044 B 美しい文字列  /
# https://atcoder.jp/contests/abc044/tasks/abc044_b
#
def getString():
    return input()


def main():
    data = getString()

    d = dict()
    f = True

    for c in list(data):
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1

    for v in d.values():
        if v % 2 == 1:
            f = False
            break

    if f == True:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
