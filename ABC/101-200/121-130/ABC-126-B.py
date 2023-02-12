# ABC-126 B - YYMM or MMYY
# https://atcoder.jp/contests/abc126/tasks/abc126_b
#
def getString():
    return input()


def isM(x):
    return 1 <= x <= 12


def main():
    s = getString()

    a = int(s[:2])
    b = int(s[2:])

    if isM(a) and isM(b):
        print('AMBIGUOUS')
    elif isM(a):
        print('MMYY')
    elif isM(b):
        print('YYMM')
    else:
        print('NA')


if __name__ == "__main__":
    main()
