# ABC-095 A - Something on It
# https://atcoder.jp/contests/abc095/tasks/abc095_a
#
def getString():
    return input()


def main():
    s = list(getString())

    r = 700
    for t in s:
        if t == 'o':
            r += 100
    print(r)


if __name__ == "__main__":
    main()
