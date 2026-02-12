# ABC-045 B - 3人でカードゲームイージー
# https://atcoder.jp/contests/abc045/tasks/abc045_b
#
def getString() -> str:
    return input()


player_name: list[str] = ["A", "B", "C"]


def play(p: int, d: list[list[str]]) -> int:
    if len(d[p]) == 0:
        print(player_name[p])
        return -1
    else:
        v: str = d[p].pop(0)
        return 0 if v == "a" else 1 if v == "b" else 2


def main():
    d: list[list[str]] = [list(getString()), list(getString()), list(getString())]

    p: int = 0
    while p >= 0:
        p = play(p, d)


if __name__ == "__main__":
    main()
