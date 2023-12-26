n = int(input())
arr =list(map(int,input().split()))
arr.sort()
ans =0
for i in range(len(arr)):
    if arr[i]==n-i:
        ans = max(ans,arr[i])
       
print(ans)