from collections import deque
import sys
input= sys.stdin.readline
n = int(input())
ans = sys.maxsize
q= deque()
d=0
for _ in range(n):
    v1,v2 = map(int,input().split())
    q.append((v1,v2))
for j in range(n):
    if j ==0 or j ==n-1:
        s=q.popleft()
        r = q.popleft()
        q.appendleft(s)
    for i in range(len(q)-1):
        d += abs(q[i][0]-q[i+1][0])+abs(q[i][1]-q[i+1][1])
    
    ans = min(ans,d)
print(ans)