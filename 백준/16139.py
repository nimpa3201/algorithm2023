s= input()
q = int(input())
arr = []
for _  in range(q):
    key, start, end = input().split()
    ps = [0 for _ in range(len(s)+1)]
    start =int(start)
    end = int(end)
    if s[0] == key :
        ps[1]=1

    for i in range(1,len(s)):
        if s[i] == key:
            ps[i+1] =ps[i]+1
        else:
            ps[i+1] =ps[i]
    ans = ps[end+1]-ps[start]
    print(ans)
