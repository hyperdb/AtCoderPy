# ABC-274 B - Line Sensor
# https://atcoder.jp/contests/abc274/tasks/abc274_b
#
def getIntMap():
    return map(int, input().split())


def getStringListRow(N):
    return [list(list(input())) for _ in range(N)]


def main():
    h, w = getIntMap()
    c = getStringListRow(h)

    a = []
    for i in range(len(c[0])):
        tmp = []
        for v in c:
            tmp.append(v[i])
        a.append(tmp)

    b = [str(x.count('#')) for x in a]

    print(" ".join(b))


if __name__ == "__main__":
    main()
