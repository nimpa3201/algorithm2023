n = int(input())
arr = [ int(input()) for _ in range(n)]
arr.sort()
ans =0
if len(arr)==1:
    print(arr[0])
else:

    for i in range(n-1,0,-1):
        if arr[i-1] > 1:
            ans += arr[i]*arr[i-1] 
        else:
            ans +=arr[i-1]+arr[i]
print(ans)