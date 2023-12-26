n = int(input())
arr = list(map(int,input().split()))
m = int(input())
tmp=0
cnt =0
R =0
for L in range(n):
    while R+1 <= n and tmp <= m:
        tmp += arr[R]
        R +=1
    if tmp > m:
        cnt+=1
    tmp -= arr[L]
print(cnt)