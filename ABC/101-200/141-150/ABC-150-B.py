# ABC-150 B - Count ABC
# https://atcoder.jp/contests/abc150/tasks/abc150_b
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    c = 0
    for i in range(n - 2):
        if s[i:i+3] == 'ABC':
            c += 1
    print(c)


if __name__ == "__main__":
    main()
