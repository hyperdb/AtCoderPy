# ABC-104 B - AcCepted
# https://atcoder.jp/contests/abc104/tasks/abc104_b
#
def getString():
    return input()


def main():
    s = getString()

    r = True
    if s[0] != 'A':
        r = False
    elif s[2:-1].count('C') != 1:
        r = False
    elif not (s.replace('A', '').replace('C', '')).islower():
        r = False
    print('AC' if r else 'WA')


if __name__ == "__main__":
    main()
