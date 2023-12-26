n,s =map(int,input().split())
tmp = n//s
li =[]
ans =1
while len(li)<s:
    li.append(tmp)
for i in range(n%s):
    li[i]+=1

for i in li:
    ans*=i
print(ans)