import sys
import heapq
INF =sys.maxsize

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
dist = [ INF for _ in range(n)]
arr = list(map(int,input().split()))
pq = []
for _ in  range(m):
    a,b,t = map(int,input().split())
    graph[a].append((t,b))
    graph[b].append((t,a))
dist[0]=0
heapq.heappush(pq,(0,0))

def dikjstra():

    while pq :
        min_dist,min_idx = heapq.heappop(pq)

        if dist[min_idx] != min_dist or arr[min_idx]:
            continue

        for target_dist,target_idx in graph[min_idx]:
            new_dist = min_dist+target_dist
            if dist[target_idx]>new_dist:
                dist[target_idx] = new_dist
                heapq.heappush(pq,(new_dist,target_idx))

    return dist[n-1]



ans = dikjstra()
if ans == INF :
    ans =-1
print(ans)
