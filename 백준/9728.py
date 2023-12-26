t= int(input())
for k in range(t):
    n,m= map(int,input().split())
    s = set(map(int,input().split()))
    cnt=0
    for i in s:
        if m-i in s:
            cnt+=1
    print('Case #{}: {}'.format(k+1,cnt//2))