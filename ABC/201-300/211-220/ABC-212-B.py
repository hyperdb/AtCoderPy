# ABC-212 B - Weak Password
# https://atcoder.jp/contests/abc212/tasks/abc212_b
#
def getString():
    return input()


def gap(n, m):
    return (10 if n == 0 else n) - m


def main():
    x = list(map(int, getString()))
    y = [gap(x[i + 1], x[i]) for i in range(len(x) - 1)]

    r = 'Strong'
    if len(set(x)) == 1:
        r = 'Weak'
    elif len(set(y)) == 1 and sum(y) == 3:
        r = 'Weak'
    print(r)


if __name__ == "__main__":
    main()
