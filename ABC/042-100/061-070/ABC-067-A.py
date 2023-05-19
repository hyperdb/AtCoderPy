# ABC-067 A - Sharing Cookies
# https://atcoder.jp/contests/abc067/tasks/abc067_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print('Possible' if a % 3 == 0 or b %
          3 == 0 or (a + b) % 3 == 0 else 'Impossible')


if __name__ == "__main__":
    main()
