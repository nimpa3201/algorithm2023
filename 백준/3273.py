n = int(input())
arr = list(map(int,input().split()))
x= int(input())

arr.sort()

print(arr)

L ,R=0,n-1
tmp =0
cnt =0
while L < R :
    
    tmp = arr[L] + arr[R]
    
    if tmp == x:
        cnt+=1
        R-=1
        L+=1
        print(R,L)
    
    elif tmp > x :
        R-=1
    elif tmp < x:
        L +=1
print(cnt)