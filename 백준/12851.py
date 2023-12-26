from collections import deque
n,m = map(int,input().split())
visited = [ 0 for _ in range(100001)]
step = [ 0 for _ in range(100001)]
test =[ 0 for _ in range(100001)]
q = deque()
def can_go(x):
    if 0<=x<100001 and not visited[x]:
        return True
    else:
        return False



def push(x,s):
    q.append(x)
    visited[x] =1
    step[x] =s
    test[x]+=1

def bfs():
    while q:
        x = q.popleft()
        for i in [2*x,x+1,x-1]:
            if can_go(i):
                push(i,step[x]+1)
push(n,0)
bfs()
tmp1 = step[m]
a = test[m]
visited = [ 0 for _ in range(100001)]
step = [ 0 for _ in range(100001)]
test =[ 0 for _ in range(100001)]
q = deque()


def bfs1():
    while q:
        x = q.popleft()
        for i in [x+1,x-1,2*x]:
            if can_go(i):
                push(i,step[x]+1)
                
push(n,0)
bfs1()
tmp2 = step[m]
print(min(tmp1,tmp2))
if tmp1 == tmp2:
    print(visited[m]+a)
else:
    print(min(visited[m],a))