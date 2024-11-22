# ABC-052 C - Factors of Factorial
# https://atcoder.jp/contests/abc052/tasks/arc067_a
#
import math


def getInt():
    return int(input())


# cf. [素数列挙を7行で Python #Python - Qiita](https://qiita.com/FN_Programming/items/b103ca45183efcc82486)
def getPrimes(N):
    primes = [2]
    for i in range(3, N, 2):  # 偶数は除外
        all(i % p != 0 for p in primes) and primes.append(i)
    return primes


def main():
    N = getInt()
    nf = math.factorial(N)

    primes = getPrimes(N + 1)

    # cf. [ABC 052 C - Factors of Factorial のメモ](https://zenn.dev/dhirabayashi/articles/2cbe07721e9db4)
    r = 1
    for p in primes:
        c = 0
        while True:
            d, m = divmod(nf, p)
            if m == 0:
                c += 1
                nf = d
            else:
                break
        r *= c + 1  # p が c 個選択される（0個の場合を考慮して+1）
    print(r % (10**9 + 7))


if __name__ == "__main__":
    main()
