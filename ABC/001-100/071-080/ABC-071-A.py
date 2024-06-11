# ABC-071 A - Meal Delivery
# https://atcoder.jp/contests/abc071/tasks/abc071_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, a, b = getIntMap()
    print('A' if abs(a - x) <= abs(b - x) else 'B')


if __name__ == "__main__":
    main()
