# ABC-355 A - Who Ate the Cake?
# https://atcoder.jp/contests/abc355/tasks/abc355_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    if a == b:
        print(-1)
    else:
        print(6 - (a + b))


if __name__ == "__main__":
    main()
