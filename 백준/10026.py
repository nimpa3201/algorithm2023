from collections import deque
n = int(input())
visited = [ [0 for _ in range(n)] for _ in range(n)]
grid = [list(input())for _ in range(n)]
q= deque()
def can_go(x,y):
    if 0<=x<n and 0<=y<n and not visited[x][y] :
        return True
    else:
        return False
def push(x,y):
    q.append((x,y))
    visited[x][y]=1
def bfs():
    global cnt
    while q:
        x,y =q.popleft()
        dxs=[0,0,-1,1]
        dys=[1,-1,0,0]

        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y +dy
            if can_go(nx,ny) and grid[nx][ny]==grid[x][y]:
                push(nx,ny)
cnt=0
for i in range(n):
    for j in range(n):
        if can_go(i,j):
            cnt+=1
            push(i,j)
            bfs()
print(cnt,end=' ')
cnt=0
visited = [[ 0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] =='G':
            grid[i][j]='R'
for i in range(n):
    for j in range(n):
        if can_go(i,j):
            cnt+=1
            push(i,j)
            bfs()
print(cnt) 
