# ABC-056 A - HonestOrDishonest
# https://atcoder.jp/contests/abc056/tasks/abc056_a
#
def getStringMap():
    return input().split()


def main():
    a, b = getStringMap()

    if a == 'H':
        print('H' if b == 'H' else 'D')
    else:
        print('D' if b == 'H' else 'H')


if __name__ == "__main__":
    main()
