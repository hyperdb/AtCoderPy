# ABC-043 B - バイナリハックイージー
# https://atcoder.jp/contests/abc043/tasks/abc043_b
#
def getString() -> str:
    return input()


def kb_proc(k: str, buf: str) -> str:
    if k == "B":
        if len(buf) > 0:
            buf = buf[:-1]
    else:
        buf += k
    return buf


def main():
    S: str = getString()

    v: str = ""
    for c in list(S):
        v = kb_proc(c, v)
    print(v)


if __name__ == "__main__":
    main()
