# ABC-043 B - バイナリハックイージー
# https://atcoder.jp/contests/abc043/tasks/abc043_b
#
def getString():
    return input()


def kb_proc(k, buf):
    if (k == 'B'):
        if (len(k) > 0):
            buf = buf[:-1]
    else:
        buf += k
    return buf


def main():
    d = getString()
    v = ''

    for c in list(d):
        v = kb_proc(c, v)
    print(v)


if __name__ == "__main__":
    main()
