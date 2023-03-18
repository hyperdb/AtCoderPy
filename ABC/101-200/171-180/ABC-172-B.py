# ABC-172 B - Minor Change
# https://atcoder.jp/contests/abc172/tasks/abc172_b
#
def getString():
    return input()


def main():
    s = list(getString())
    t = list(getString())

    c = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
