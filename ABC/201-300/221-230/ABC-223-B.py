# ABC-223 B - String Shifting
# https://atcoder.jp/contests/abc223/tasks/abc223_b
#
def getString():
    return input()


def main():
    s = getString()

    if len(s) == 1:
        print(s)
        print(s)
    else:
        t = s
        l = []
        for i in range(len(s)):
            t = t[1:] + t[0]
            l.append(t)
        l.sort()
        print(l[0])
        print(l[-1])


if __name__ == "__main__":
    main()
