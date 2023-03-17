# ABC-170 B - Crane and Turtle
# https://atcoder.jp/contests/abc170/tasks/abc170_b
#
def getIntMap():
    return map(int, input().split())


def main():
    x, y = getIntMap()

    # x = a + b
    # y = 2a + 4b
    a = (4 * x - y) // 2
    b = x - a

    if y % 2 == 1:
        print('No')
    elif a >= 0 and b >= 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
