# ABC-240 A - Edge Checker
# https://atcoder.jp/contests/abc240/tasks/abc240_a
#
def getIntMap():
    return map(int, input().split())

def main():
    a, b = getIntMap()

    print('Yes' if abs(a - b) == 1 or abs(a % 10 - b % 10) == 1 else 'No')


if __name__ == "__main__":
    main()