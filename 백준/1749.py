import sys
n,m = map(int,input().split())
arr = [[0 for _ in range(m+1)]]+[[0]+list(map(int,input().split())) for _ in range(n)]
dp = [[ 0 for _ in range(m+1)] for _ in range(n+1)]
ans = -sys.maxsize
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+arr[i][j]

for x1 in range(1,n+1):
    for y1 in range(1,m+1):
        for x2 in range(x1,n+1):
            for y2 in range(y1,m+1):
                ans = max(ans,dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])
        
print(ans)