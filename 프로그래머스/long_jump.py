def solution(n):
    if n <3 :
        return n
    else:
        dp = [0 for _ in range(n+1)]
        dp[1]=1
        dp[2]=2
        if n <=3 :
            return dp[n]

        for i in range(3,n+1):
            dp[i]=dp[i-1]%1234567+dp[i-2]%1234567
        return dp[n]%1234567

print(solution(4))
print(solution(5))
print(solution(2))
