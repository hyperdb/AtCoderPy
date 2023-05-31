# ABC-236 A - chukodai
# https://atcoder.jp/contests/abc236/tasks/abc236_a
#
def getString():
    return input()

def getIntMap():
    return map(int, input().split())

def main():
    s = list(getString())
    a, b = getIntMap()

    s[a - 1], s[b - 1] = s[b - 1], s[a - 1]

    print("".join(s))


if __name__ == "__main__":
    main()