# ABC-141 B - Tap Dance
# https://atcoder.jp/contests/abc141/tasks/abc141_b
#
def getString():
    return input()


def main():
    s = list(getString())

    l = [s[i] for i in range(1, len(s), 2)]
    r = [s[i] for i in range(0, len(s), 2)]

    if 'L' in r or 'R' in l:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    main()
