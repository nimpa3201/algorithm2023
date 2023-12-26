s =int(input())
tmp =0
ans=0
for i in range(1,s+1):
    tmp+=i
    
    if tmp <= s:
        ans =max(ans,i)
    else:
        break
print(ans)