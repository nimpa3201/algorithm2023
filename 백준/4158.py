while True:
    n,m =map(int,input().split())
    p1 = {int(input()) for _ in range(n)}
    p2 = {int(input()) for _ in range(m)}
    if n ==0 and m ==0:
        break
    cnt=0
    cnt1=0
    for i in p1:
        if i in p2:
            cnt+=1
    for i in p2:
        if i in p1:
            cnt1+=1
    print(max(cnt,cnt1))
