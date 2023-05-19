# ABC-062 B - Picture Frame
# https://atcoder.jp/contests/abc062/tasks/abc062_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    h, w = getIntMap()
    a = getStringRow(h)

    a.append('')
    a.insert(0, '')

    f = '{:#^' + str(w + 2) + 's}'

    for i in range(len(a)):
        print(f.format(a[i]))


if __name__ == "__main__":
    main()
