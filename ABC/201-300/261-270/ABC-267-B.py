# ABC-267 B - Split?
# https://atcoder.jp/contests/abc267/tasks/abc267_b
#
def getString():
    return input()


def col(p):
    c = []
    c.append(0)
    c.append(p[7])
    c.append(p[4])
    c.append(1 if sum([p[2], p[8]]) > 0 else 0)
    c.append(1 if sum([p[1], p[5]]) > 0 else 0)
    c.append(1 if sum([p[3], p[9]]) > 0 else 0)
    c.append(p[6])
    c.append(p[10])

    return "".join(list(map(str, c)))


def main():
    a = [0] + list(map(int, list(getString())))
    b = ['101', '1001', '10001', '100001', '1000001']
    c = col(a)

    r = False
    if a[1] == 0:
        for s in b:
            if c.find(s) >= 0:
                r = True
                break
    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
