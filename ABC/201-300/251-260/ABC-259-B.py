# ABC-249 B - Counterclockwise Rotation
# https://atcoder.jp/contests/abc259/tasks/abc259_b
#
import math


def getIntMap():
    return map(int, input().split())


def main():
    a, b, d = getIntMap()

    r = math.radians(d)

    x = a * math.cos(r) - b * math.sin(r)
    y = a * math.sin(r) + b * math.cos(r)

    print(x, y)


if __name__ == "__main__":
    main()
