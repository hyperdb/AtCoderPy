# ABC-075 C - Bridge
# https://atcoder.jp/contests/abc075/tasks/abc075_c
#
class UnionFind:
    def __init__(self, n):
        # 親要素の番号を格納。自身が親（根）の場合は -1 * そのグループのサイズ を格納
        self.parents = [-1] * n

    def find(self, x):
        """要素xが属するグループの根を返す"""
        if self.parents[x] < 0:
            return x
        else:
            # 経路圧縮：親を根に貼り替える
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """要素xとyが属するグループを併合する"""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        # Union by Size: サイズが大きい方に小さい方を繋げる
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def size(self, x):
        """要素xが属するグループのサイズを返す"""
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """xとyが同じグループに属するかを返す"""
        return self.find(x) == self.find(y)


#
#
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M = getIntMap()
    ab = getIntListRow(M)
    a = [x[0] - 1 for x in ab]
    b = [x[1] - 1 for x in ab]

    result = 0
    # 各辺を1本ずつ取り除いてみて、連結でなくなるか確認
    for i in range(M):
        uf = UnionFind(N)
        for j in range(M):
            # 取り除く辺はスキップ
            if i == j:
                continue
            # 辺をUnionFindに追加
            uf.union(a[j], b[j])

        # 取り除いた辺の両端が連結でなければ橋
        if uf.same(a[i], b[i]) is False:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
