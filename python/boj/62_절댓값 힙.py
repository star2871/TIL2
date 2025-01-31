import sys
import heapq

sys.stdin = open("62_절댓값 힙.txt")

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))
