from collections import deque
n = int(input())
arr = list(map(int,input().split()))
visited = [0 for _ in range(n)]
step= [0 for _ in range(n)]
q= deque()

def push(n,s):
    q.append(arr[n])
    visited[n] = 1
    step[n]=s
    

def can_go(x):
    if 0<=x<n :
        return True
    else:
        return False



def bfs():
    while q:
        num =q.popleft()
        for i in range(1,num+1):
            nx =num+i
            if can_go(nx):
                push(nx,step[num]+1)

push(0,0)
bfs()
print(step)
print(visited)