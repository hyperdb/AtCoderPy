# ABC-139 B - Power Socket
# https://atcoder.jp/contests/abc139/tasks/abc139_b
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    c = 1
    i = 0
    while c < b:
        c += a - 1
        i += 1
    print(i)


if __name__ == "__main__":
    main()
