# ABC-387 B - 9x9 Sum
# https://atcoder.jp/contests/abc387/tasks/abc387_b
#
def getInt():
    return int(input())


def main():
    X = getInt()

    a = []
    for i in range(1, 10):
        a += [x * i for x in range(1, 10)]

    c = a.count(X)

    print(sum(a) - c * X)


if __name__ == "__main__":
    main()
