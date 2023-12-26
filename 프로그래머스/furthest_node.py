from collections import deque

def solution(n, edge):
    global q ,graph,visited,step
    visited = [ 0 for _ in range(n+1)]

    step = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    q =deque()
    for i ,j in edge:
        graph[i].append(j)
        graph[j].append(i)

    visited[1]=1
    for i in graph[1]:
        push(i,1)
    dfs()
    return step.count((max(step)))

def push(x,s):
    q.append(x)
    visited[x] =1
    step[x]=s

def dfs():
    while q:
        x = q.popleft()
        visited[x]=1
        for i in graph[x]:
            if can_go(i) :
                push(i,step[x]+1)
                visited[i]=1




def can_go(x):
    global visited
    if visited[x] ==0:
        return True
    else:
        return False 


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) #3