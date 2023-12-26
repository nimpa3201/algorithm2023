import sys
n = int(input())
arr= list(map(int,input().split()))
arr.sort()
ans = sys.maxsize
ans1 =0
for i in range(len(arr)):
    tmp=0
    for j in range(len(arr)):
        tmp+=abs(arr[i]-arr[j])
    if tmp <ans:
        ans = tmp
        ans1 =arr[i]
print(ans1)
        