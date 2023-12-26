n = int(input())
k = int(input())
recommand = list(map(int,input().split()))
d =dict()

for i in range(len(recommand)):
    if recommand[i]  in d:
        d[recommand[i]][0]+=1
    else:
        if len(d) <n:
            d[recommand[i]] =[1,i]
        else:
            del_list = sorted(d.items(), key =lambda x: (x[1][0],x[1][1]))
            del_key = del_list[0][0]
            del d[del_key]
            d[recommand[i]] =[1,i]


ans =[]
for i in d:
    ans.append(i)
ans.sort()
print(*ans)