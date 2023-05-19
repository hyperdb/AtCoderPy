# ABC-145 B - Echo
# https://atcoder.jp/contests/abc145/tasks/abc145_b
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    f = False
    if n % 2 == 0:
        if s[0:n//2] == s[n//2:]:
            f = True
    print('Yes' if f else 'No')


if __name__ == "__main__":
    main()
