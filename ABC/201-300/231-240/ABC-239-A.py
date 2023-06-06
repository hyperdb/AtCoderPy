# ABC-239 A - Horizon
# https://atcoder.jp/contests/abc239/tasks/abc239_a
#
import math

def getInt():
    return int(input())

def d(x):
    return math.sqrt(x * (12800000 + x))

def main():
    h = getInt()

    print(d(h))

if __name__ == "__main__":
    main()