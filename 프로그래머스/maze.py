from collections import deque


def solution(maps):
    global a,b,q,visited,step,tmp
    a=len(maps)
    b=len(maps[0])
    q =deque()
    tmp =list()
    visited = [[0 for _ in range(len(maps[1]))] for _ in range(len(maps))]
    step = [[0 for _ in range(len(maps[1]))] for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[1])):
            if maps[i][j] =='L':
                tmp.append((i,j))
    
    
    
    for i in range(len(maps)):
        for j in range(len(maps[1])):
            if maps[i][j] =='E':
                tmp.append((i,j))
    
    q =deque()

    for i in range(len(maps)):
        for j in range(len(maps[1])):
            if maps[i][j] == 'S':
               q.append((i,j))
               StoL=bfs(maps,tmp[0][0],tmp[0][1])
    
    
    q =deque()
    visited = [[0 for _ in range(len(maps[1]))] for _ in range(len(maps))]
    step = [[0 for _ in range(len(maps[1]))] for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[1])):
            if maps[i][j] == 'L':
               q.append((i,j))
               LtoE =bfs(maps,tmp[1][0],tmp[1][1])
    if StoL == False or LtoE == False:
        ans =-1
    
    else:
        ans =  StoL+LtoE 
                    
    return ans
                
                
                
def can_go(x,y,maps):
    if 0<=x<a and 0<=y<b and maps[x][y] !='X' and not visited[x][y]:
        return True
    else:
        return False

def push(x,y,s):
    q.append((x,y))
    visited[x][y] = 1
    step[x][y]=s




def bfs(maps,l,r):
    global q
    while q:
        x,y = q.popleft()
        if l == x and r ==y:
            return step[x][y]
        dxs = [0,0,1,-1]
        dys=[-1,1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny,maps): 
                push(nx,ny,step[x][y]+1) # 저에 있던 step 에 1 을 더한다
    return False
              
              
             
                
              
               
                
    
print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]) )#16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))	#-1
print(solution(["OOOOOL", "OXOXOO", "OOSXOX", "OXXXOX", "EOOOOX"])) #14
print(solution(["XXXXXL", "XXXXOO", "OOSXOX", "OXXXOX", "EOOOOX"]) )#22
print(solution(["XXXXL", "XOOSX", "XXXXX", "XXXOO", "EXXXX", "XXXXX"])) #-1




from collections import deque


def solution(maps):
    global a,b,q,visited,step,tmp
    a=len(maps)
    b=len(maps[0])
    q =deque()
    tmp =list()
    visited = [[0 for _ in range(b)] for _ in range(a)]
    step = [[0 for _ in range(b)] for _ in range(a)]
    
    L = None
    E = None
    
    for i in range(a):
        for j in range(b):
            if maps[i][j] =='L':
                L = (i,j)
            if maps[i][j] == 'E':
                E = (i,j)
    
    q =deque()
    visited = [[0 for _ in range(b)] for _ in range(a)]
    step = [[0 for _ in range(b)] for _ in range(a)]
    for i in range(a):
        for j in range(b):
            if maps[i][j] == 'S':
                q.append((i,j))
                StoL=bfs(maps,L[0], L[1])
    
    
    q =deque()
    visited = [[0 for _ in range(b)] for _ in range(a)]
    step = [[0 for _ in range(b)] for _ in range(a)]
    for i in range(a):
        for j in range(b):
            if maps[i][j] == 'L':
                q.append((i,j))
                LtoE =bfs(maps,E[0], E[1])
    if StoL == -1 or LtoE == -1:
        ans =-1
    
    else:
        ans =  StoL+LtoE 
                    
    return ans
                
                
                
def can_go(x,y,maps):
    if 0<=x<a and 0<=y<b and maps[x][y] !='X' and not visited[x][y]:
        return True
    else:
        return False

def push(x,y,s):
    q.append((x,y))
    visited[x][y] = 1
    step[x][y]=s




def bfs(maps,l,r):
    global q
    while q:
        x,y = q.popleft()
        if l == x and r ==y:
            return step[x][y]
        dxs = [0,0,1,-1]
        dys=[-1,1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny,maps): 
                push(nx,ny,step[x][y]+1) # 저에 있던 step 에 1 을 더한다
    return -1
              
              