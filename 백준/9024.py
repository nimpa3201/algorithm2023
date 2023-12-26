import sys
t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    L =0
    R = n-1
    tmp = sys.maxsize

    while L < R :
        v = arr[L]+arr[R]
        if tmp > abs(k-v):
            tmp = abs(k-v)
            cnt=0

        if v <k:
            if(abs(k-v))==tmp:
                cnt+=1
            L+=1
        elif v>k :
            if (abs(k-v)) ==tmp:
                cnt+=1

            R-=1
        else:
            cnt+=1
            L+=1
            R-=1
    print(cnt)

