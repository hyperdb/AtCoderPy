# ABC-071 B - Not Found
# https://atcoder.jp/contests/abc071/tasks/abc071_b
#
def getString():
    return input()


def az_array():
    c = ord('a')
    l = []
    for i in range(26):
        l.append(chr(c + i))
    return l


def main():
    s = list(getString())
    t = list(set(s))
    t.sort()

    r = 'None'
    for c in az_array():
        if not c in t:
            r = c
            break
    print(r)


if __name__ == "__main__":
    main()
