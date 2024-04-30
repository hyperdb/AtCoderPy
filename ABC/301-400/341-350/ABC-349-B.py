# ABC-349 B - Commencement
# https://atcoder.jp/contests/abc349/tasks/abc349_b
#
def getString():
    return input()


def main():
    s = getString()

    d = dict()
    for c in s:
        d.setdefault(c, 0)
        d[c] += 1

    c = dict()
    for i in d.values():
        c.setdefault(i, 0)
        c[i] += 1

    b = [0 if x == 2 else 1 for x in c.values()]

    print('Yes' if sum(b) == 0 else 'No')


if __name__ == "__main__":
    main()
