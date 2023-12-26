import sys
input =sys.stdin.readline
t= int(input())

for _ in range(t):
    d,n =map(int,input().split())
    arr =[0]+list(map(int,input().split()))
    cnt=0
    for i in range(1,n+1):
        arr[i] =arr[i]+arr[i-1]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[j]-arr[i])%d ==0:
                cnt+=1
               
    print(cnt)