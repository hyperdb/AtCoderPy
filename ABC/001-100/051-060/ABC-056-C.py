# ABC-056 C - Go Home
# https://atcoder.jp/contests/abc056/tasks/arc070_a
#
def getInt():
    return int(input())


def main():
    X = getInt()

    p = 0
    i = 0
    # 位置pはi分進む
    while p < X:
        i += 1
        p += i
    print(i)


if __name__ == "__main__":
    main()
