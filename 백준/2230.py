import sys
n,m = map(int,input().split())
arr= [int(input()) for _ in range(n)]
arr.sort()
L,R =0, 1
ans = sys.maxsize
while L < n and R <n:
    tmp = arr[R]-arr[L]

    if tmp ==m:
        print(m)
        break
    elif tmp > m :
        L+=1
        ans = min(ans,tmp)
    else:
        R+=1
if ans !=m:
    print(ans)