# ABC-052 B - Increment Decrement
# https://atcoder.jp/contests/abc052/tasks/abc052_b
#
def getString():
    return input()


def getInt():
    return int(input())


def main():
    n = getInt()
    buf = list(getString())

    x = 0
    m = 0
    for s in buf:
        x = x + (1 if s == 'I' else - 1)
        m = x if x > m else m
    print(m)


if __name__ == "__main__":
    main()
