import sys
input = sys.stdin.readline
t = int(input())
ans =0
ans1=[]
ans4=[]
for _ in range(t):
    d=[]
    n =int(input())
    arr = list(map(int,input().split()))
    tmp =0
    dp = [0 for _ in range(n+1)]
    dp[1] =arr[0]
    for i in range(n):
        dp[i+1] =dp[i]+arr[i]
    for i in range(n+1):
        for j in range(i,n+1):
            if tmp <=dp[j]-dp[i]:
                
                tmp =dp[j]-dp[i]
                d.append((i+1,j))
            
        ans3 =[]            
        d.sort(key = lambda x :-abs((x[0]-x[1])))
        for i,j in d:
            if tmp ==dp[j]-dp[i-1]:
                ans3.append((i,j))
    ans4.append(ans3[-1])
    ans += tmp
print(ans)
for i ,j in ans4:
    print(i,j)

