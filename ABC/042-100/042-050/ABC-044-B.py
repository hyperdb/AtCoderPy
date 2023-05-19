# ABC-044 B 美しい文字列  /
# https://atcoder.jp/contests/abc044/tasks/abc044_b
#
def getString():
    return input()


def main():
    buf = list(getString())

    d = dict()
    f = True

    for c in buf:
        d[c] = d[c] + 1 if c in d else 1

    for v in d.values():
        if v % 2 == 1:
            f = False
            break

    print('Yes' if f == True else 'No')


if __name__ == "__main__":
    main()
