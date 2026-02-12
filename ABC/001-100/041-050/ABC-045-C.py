# ABC-045 C - たくさんの数式
# https://atcoder.jp/contests/abc045/tasks/arc061_a
#
import itertools


def getString() -> str:
    return input()


def main():
    S: list[str] = list(getString())
    T: list[int] = [i for i in range(len(S) - 1)]

    m: int = 0
    for i in range(len(T)):
        # `+`の入る位置を組み合わせで求める
        for t in list(itertools.combinations(T, i + 1)):
            n: int = 0
            for j in range(len(S)):
                # `+`に出会うまで桁繰り上げ
                n = n * 10 + int(S[j])
                if j in t:
                    m += n
                    n = 0
            m += n
    m += int("".join(S))
    print(m)


if __name__ == "__main__":
    main()
