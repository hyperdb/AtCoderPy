# ABC-451 C - Understory
# https://atcoder.jp/contests/abc451/tasks/abc451_c
#
import heapq


def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    Q = getInt()
    query = getIntListRow(Q)
    # ヒープを用いて、クエリを処理する
    heap = []
    heapq.heapify(heap)

    for t, h in query:
        # t = 1 のとき、ヒープに h を追加する
        if t == 1:
            heapq.heappush(heap, h)
        # t = 2 のとき、ヒープから h を取り除く
        else:
            # ヒープが空、またはヒープの最小値が h より大きい場合は、何もしない
            if not heap or heap[0] > h:
                pass
            # そうでない場合は、ヒープの最小値が h 以下になるまで、ヒープから値を取り除く
            else:
                while heap[0] <= h:
                    heapq.heappop(heap)
                    if not heap:
                        break
        # クエリの処理が終わった後、ヒープのサイズを出力する
        print(len(heap))


if __name__ == "__main__":
    main()
