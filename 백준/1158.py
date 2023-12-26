from collections import deque
n,k = map(int,input().split())
num = [ i for i in range(1,n+1)]
num =deque(num)
ans=[]
print("<",end="")
while num:
    for i in range(k-1):
        num.append(num.popleft())
  
    ans.append(num.popleft())
for i in ans[:-1]:
    print(i,end=', ')
print(ans[-1],end="")
print(">")