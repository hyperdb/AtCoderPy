# ABC-083 B - Some Sums
# https://atcoder.jp/contests/abc083/tasks/abc083_b
#
def getIntMap():
    return map(int, input().split())


def main():
    n, a, b = getIntMap()

    r = 0
    for i in range(1, n + 1):
        s = sum(map(int, list(str(i))))
        if s >= a and s <= b:
            r += i
    print(r)


if __name__ == "__main__":
    main()
