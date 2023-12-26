import heapq
import sys
INF = sys.maxsize
n,m = map(int,input().split())
arr = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((c,b))
    arr[b].append((c,a))
s,t = map(int,input().split())
dist = [INF for _ in range(n+1)]
pq =[]

def dijkkstra(start,end):
    dist[start] =0
    heapq.heappush(pq,(0,start))

    while pq:
        min_dist,min_index =heapq.heappop(pq)

        if dist[min_index] != min_dist:
            continue
   
        for target_dist ,target_index in arr[min_index]:
            new_dist = min_dist+target_dist
            if new_dist < dist[target_index]:
                dist[target_index]=new_dist
                heapq.heappush(pq,(new_dist,target_index))
    return dist[end]
print(dijkkstra(s,t))