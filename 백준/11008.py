t = int(input())

for _ in range(t):
    s,p = input().split()
    key = len(p)
    cnt=0
    
    for i in range(len(s)):
        if s[i:i+key] ==p:
            cnt+=1
    print(cnt+len(s)-(cnt*key))