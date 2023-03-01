# ABC-152 B - Comparing Strings
# https://atcoder.jp/contests/abc152/tasks/abc152_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    s = ["".join([str(a) for _ in range(b)]),
         "".join([str(b) for _ in range(a)])]
    s.sort()

    print(s[0])


if __name__ == "__main__":
    main()
