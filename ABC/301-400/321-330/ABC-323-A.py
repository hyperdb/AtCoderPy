# ABC-323 A - Weak Beats 
# https://atcoder.jp/contests/abc323/tasks/abc323_a
#
def getString():
    return input()


def main():
    s = getString()
    a = list(map(int, [s[x] for x in range(len(s)) if x % 2 == 1]))

    print('Yes' if sum(a) == 0 else 'No')


if __name__ == "__main__":
    main()
