from collections import deque
n,m,k = map(int,input().split())
arr = [[ 0 for _ in range(m)]for _ in range(n)]
visited= [[ 0 for _ in range(m)]for _ in range(n)]
q= deque()
cnt=1
ans=0
for _ in range(k):
    r,c = map(int,input().split())
    arr[r-1][c-1] =1


def push(x,y):
    visited[x][y] = 1
    q.append((x,y))

def bfs():
    global cnt
    cnt=1
    while q:
        x,y =q.popleft()
        dxs =[0,0,-1,1]
        dys =[1,-1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny):
                push(nx,ny)
                cnt+=1

def can_go(x,y):
    if 0<=x<n and 0<=y<m and not visited[x][y] and arr[x][y]:
        return True
    else:
        return False 








for i in range(n):
    for j in range(m):
        if can_go(i,j):
            push(i,j)
            bfs()
            ans= max(ans,cnt)
print(ans)