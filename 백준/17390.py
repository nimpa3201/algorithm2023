import sys

input =sys.stdin.readline
n ,q = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort(reverse = False)
pr =[0 for _ in range(n+1)]
pr[1] = nums[0]

for i in range(2,n+1):
    pr[i] = pr[i-1]+nums[i-1]

for _ in range(q):
    s,e  = map(int,input().split())
    print(pr[e]-pr[s-1])
