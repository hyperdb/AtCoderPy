# ABC-214 B - How many?
# https://atcoder.jp/contests/abc214/tasks/abc214_b
#
def getIntMap():
    return map(int, input().split())


def main():
    s, t = getIntMap()

    c = 0
    for i in range(s + 1):
        for j in range(s + 1 - i):
            for k in range(s + 1 - i - j):
                if i * j * k <= t:
                    c += 1
    print(c)


if __name__ == "__main__":
    main()
