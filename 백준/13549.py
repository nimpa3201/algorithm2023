from collections import deque
q =deque()
n,k = map(int,input().split())
visited = [ 0 for _ in range(100001)]
step = [ 0 for _ in range(100001)]
if n == k :
    print(0)
    exit()
def can_go(x):
    if 0<=x<=100000 and not visited[x]:
        return True
    else:
        return False

def push(x,s):
    q.append(x)
    visited[x]=1
    step[x]=s


def bfs():
    while q:    
        x=q.popleft()
        for i in [2*x]:
            if can_go(i):
                push(i,step[x])
        for i in [x-1,x+1]:
            if can_go(i):
                push(i,step[x]+1)
    
q.append(n)
bfs()
print(step[k])