# ABC-043 B - バイナリハックイージー
# https://atcoder.jp/contests/abc043/tasks/abc043_b
#
def getString():
    return input()


def kb_proc(key, buf):
    if (key == 'B'):
        if (len(key) > 0):
            buf = buf[:-1]
    else:
        buf += key
    return buf


def main():
    data = getString()
    value = ''

    for c in list(data):
        value = kb_proc(c, value)
    print(value)


if __name__ == "__main__":
    main()
