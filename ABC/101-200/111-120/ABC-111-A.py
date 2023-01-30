# ABC-111 A - AtCoder Beginner Contest 999
# https://atcoder.jp/contests/abc111/tasks/abc111_a
#
def getString():
    return input()


def main():
    n = list(getString())

    s = ''
    for c in n:
        s += '1' if c == '9' else '9'
    print(s)


if __name__ == "__main__":
    main()
