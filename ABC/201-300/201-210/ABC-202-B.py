# ABC-202 B - 180°
# https://atcoder.jp/contests/abc202/tasks/abc202_b
#
def getString():
    return input()


def main():
    s = list(getString())

    s.reverse()
    t = ['6' if c == '9' else '9' if c == '6' else c for c in s]

    print("".join(t))


if __name__ == "__main__":
    main()
