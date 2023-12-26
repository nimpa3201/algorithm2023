import sys
import heapq
INF = sys.maxsize
vertice,edge =map(int,input().split()) # 정점, 간선
start = int(input())
dist = [INF for _ in range(vertice+1)]
graph = [[] for _ in range(vertice+1)]
visited = [False for _ in range(vertice+1)]
pq = []

for i in range(edge):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
dist[start] =0

heapq.heappush(pq,(0,start))


def Dijkstra():
    
    while pq:
        min_dist,min_index = heapq.heappop(pq)
        
        if dist[min_index] != min_dist:
            continue
        
        for target_dist,target_index in graph[min_index]:
        
            new_dist = min_dist+target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist           
                heapq.heappush(pq,(new_dist,target_index))
Dijkstra()
                
for i in dist[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)
               
'''
graph = [
    [],  # 0번 인덱스는 사용하지 않습니다.
    [(1, 2), (2, 5)],  # 1번 도시와 연결된 간선
    [(4, 3)],  # 2번 도시와 연결된 간선
    [(2, 4)],  # 3번 도시와 연결된 간선
    [(3, 5)]  # 4번 도시와 연결된 간선
]
'''
        
        
        
    
           

