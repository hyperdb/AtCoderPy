# ABC-352 B - Typing
# https://atcoder.jp/contests/abc352/tasks/abc352_b
#
def getString():
    return input()


def main():
    s = getString()
    t = getString()

    r = []
    p = 0
    for i in range(len(s)):
        y = t[p:].index(s[i])
        p += y
        r.append(p)
        p += 1

    print(" ".join(map(str, [i + 1 for i in r])))


if __name__ == "__main__":
    main()
