# ABC-187 A - Large Digits
# https://atcoder.jp/contests/abc187/tasks/abc187_a
#
def getIntMap():
    return map(int, input().split())


def s(x):
    return sum(map(int, list(str(x))))


def main():
    a, b = getIntMap()

    print(max(s(a), s(b)))


if __name__ == "__main__":
    main()
