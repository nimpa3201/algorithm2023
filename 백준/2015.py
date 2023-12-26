n,k = map(int,input().split())
arr= list(map(int,input().split()))
record = {0:1}
tmp =0
ans =0
for i in arr:
    tmp +=i

    if tmp-k in record.keys():
        ans += record[tmp-k]

    if tmp in record.keys():
        record[tmp]+=1
    else:
        record[tmp]=1 

print(ans)