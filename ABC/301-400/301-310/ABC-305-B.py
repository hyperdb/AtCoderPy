# ABC-305 B - ABCDEFG
# https://atcoder.jp/contests/abc305/tasks/abc305_b
#
def getStringMap():
    return input().split()


def main():
    p, q = getStringMap()
    d = [3, 1, 4, 1, 5, 9]
    s = ord(p) - ord('A')
    e = ord(q) - ord('A')

    print(abs(sum(d[:s]) - sum(d[:e])))


if __name__ == "__main__":
    main()
