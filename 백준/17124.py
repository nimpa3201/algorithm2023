import sys
t= int(input())
ans = sys.maxsize
for _ in range(t):
    c =[]
    n,m = map(int,input().split())
    a=list(map(int,input().split()))
    b =list(map(int,input().split()))
    for i in range(n):
        for j in range(m):
            tmp=abs(a[i]-b[i])
            if ans > tmp:
                ans = tmp
                c.append(b[i])
    print(sum(c))
