from collections import deque 
num = int(input())
grid = [list(map(int,input().split())) for _ in range(num)]
maxval = 0
for i in range(num):
    for j in range(num):
        maxval = max(maxval,grid[i][j])

def can_go(limit,col,row):
    if  0<=col<num and 0<=row<num and not visited[col][row] and grid[col][row]>=limit:
        return True
    else:
        return False

def bfs(limit):
    #visited[col][row] = True
    while q:
        dxs = [1,-1,0,0]
        dys =[0,0,-1,1]
        x,y = q.popleft()
        for dx, dy in zip(dxs,dys):
       
            nx = x+dx
            ny = y+dy
            if can_go(limit,nx,ny):
               
                visited[nx][ny] = True
                q.append((nx,ny))



ans =0
for i in range(1,maxval+1):
    q = deque()
    cnt =0
    visited = [[False for _ in range(num)] for _ in range(num)]
    for j in range(num):
        for k in range(num):        
            if can_go(i,j,k):
                q.append((j,k))
                visited[j][k] = True
                cnt+=1
                bfs(i)
    ans = max(ans,cnt)
print(ans)


# def can_go(limit,col,row):
#     if limit>=grid[col][row] and 0<=col<num and 0<=row<num and not visited[col][row]:
#         return True
#     else:
#         return False