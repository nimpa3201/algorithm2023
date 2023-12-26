from collections import deque
A,B,N,M = map(int,input().split())
visited = [ 0 for _ in range(100001)]
q = deque()
step =[ 0 for _ in range(100001)]

def push(x,s):
    visited[x] = 1
    q.append(x)
    step[x] = s+1 


def can_go(x):
    if 0<=x<100001 and not visited[x]:
        return True
    else:
        return False



def bfs():
    while q:
        x= q.popleft()
        for i in [-1,1,+A,-A,+B,-B]:
            nx = x+i
            if can_go(nx):
                push(nx,step[x])
        for i in [A,B]:
            nx = x*i
            if can_go(nx):
                push(nx,step[x])
            
q.append(N)
bfs()
print(step[M])   
 

