from collections import deque
r,c = map(int,input().split())
grid = [list(input()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
q = deque()
empty = []
cnt =0

def can_go (x,y):
    if 0<=x<r and 0<= y< c and  visited[x][y] ==0 and grid[x][y] !='#':
        return True
    else:
        return False 

def push(x,y):
    q.append((x,y))
    visited[x][y] = 1
    
def bfs():
    global cnt
    cnt=0
    while q:
        x,y = q.popleft()
        dxs = [0,0,-1,1]
        dys=[1,-1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny):
                push(nx,ny)
                cnt+=1



for i in range(r):
    for j in range(c):       
        if can_go (i,j):
            push(i,j)
            bfs()
            empty.append(cnt)
print(empty)