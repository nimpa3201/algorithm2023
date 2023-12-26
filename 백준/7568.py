n = int(input())
arr= []
ans =[]
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))


for i in range(len(arr)):
    cnt=0
    for j in range(len(arr)):
        x,y = arr[i]
        p,q = arr[j]
        if (x<p and y<q)  :
            cnt+=1
    ans.append(cnt+1)
print(*ans)

