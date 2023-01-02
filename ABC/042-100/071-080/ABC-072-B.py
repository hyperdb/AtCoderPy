# ABC-072 B - OddString
# https://atcoder.jp/contests/abc072/tasks/abc072_b
#
def getString():
    return input()


def main():
    s = list(getString())

    r = ''
    for i in range(len(s)):
        if i % 2 == 0:
            r += s[i]
    print(r)


if __name__ == "__main__":
    main()
