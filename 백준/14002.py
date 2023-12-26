n = int(input())
arr = list(map(int,input().split()))
dp = [ 1 for _ in range(n)]
ans =[]
for i in range(len(arr)):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] =max(dp[i],dp[j]+1)
        
print(max(dp))
tmp =max(dp)


for i in range(n-1,-1,-1):
    if dp[i] == tmp:
        ans.append(arr[i])
        tmp-=1
ans.reverse()
print(*ans)