n,m = map(int,input().split())
arr =[0]+list(map(int,input().split()))
ans=[]
visited = [0] * (n+1)
cnt=0
def dfs(num,tmp):
    global cnt
    if num == n+1 :
        return
    tmp+=arr[num]

    if tmp == m:
        cnt+=1
        
    dfs(num+1,tmp)
    dfs(num+1,tmp-arr[num])
dfs(1,0)
print(cnt)