# ABC-146 B - ROT N
# https://atcoder.jp/contests/abc146/tasks/abc146_b
#
def getInt():
    return int(input())


def getString():
    return input()


def conv(c, n):
    x = ord(c) + n
    return chr(x if x <= ord('Z') else x - 26)


def main():
    n = getInt()
    s = list(getString())

    print("".join([conv(c, n) for c in s]))


if __name__ == "__main__":
    main()
