# ABC-333 B - Pentagon
# https://atcoder.jp/contests/abc333/tasks/abc333_b
#
def getString():
    return input()


def distance(p1, p2):
    v1 = ord(p1)
    v2 = ord(p2)

    v = v1 - v2 if v1 >= v2 else v2 - v1

    return min(v, 5 - v)


def main():
    s1, s2 = list(getString())
    t1, t2 = list(getString())

    print('Yes' if distance(s1, s2) == distance(t1, t2) else 'No')


if __name__ == "__main__":
    main()
