n = int(input())
arr =[]
grid = [[] for _ in range(n)]
visited = [0 for _ in range(n)] 
for _ in range(n):
    li = list(map(int,input().split()))
    arr.append(li)

for i in range(len(li)):
    for j in range(len(li)):
        if arr[i][j] ==1:
            grid[i].append(j)
print(grid)

def dfs(n):
    visited[n] = 1
    for next in grid[n]:
        if not grid[next]:
            visited[next] = 1
            dfs(next)

dfs(0)
print(visited)