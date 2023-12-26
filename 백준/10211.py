import sys
t = int(input())
for _ in range(t):
    ans= - sys.maxsize
    n = int(input())
    arr = [0]+list(map(int,input().split()))
    pr = [0 for _ in range(n+1)]
    pr[1]=arr[1] 
    for i in range(2,n+1):
        pr[i] = pr[i-1]+arr[i]
    for i in range(n+1):
        for j in range(i+1,n+1):
            ans = max(ans,pr[j]-pr[i])
    print(ans)
