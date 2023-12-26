from collections import deque
m,n = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
q = deque()
def push(x,y):
    q.append((x,y))
    visited[x][y]+=1


def can_go(nx,ny,x,y):
    if 0<=x<m and 0<=y<n and 0<=nx<m and 0<=ny<n and grid[x][y]>grid[nx][ny]:
        return True
    else:
        return False



def bfs():
    while q:
        x,y =q.popleft()
        dxs =[0,0,1,-1]
        dys =[1,-1,0,0]
        
        for dx,dy in zip(dxs,dys):
            nx = x+dx 
            ny = y+dy
            if can_go(nx,ny,x,y):
                push(nx,ny)   
    
    
push(0,0)
bfs()
print(visited[m-1][n-1])