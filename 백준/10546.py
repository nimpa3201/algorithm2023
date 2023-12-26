n = int(input())
d =dict()
for _ in range(n):
    name =input()
    if name not in d:
        d[name] =1
    else:
        d[name] +=1
for _ in range(n-1):
    a = input()
    if a in d:
        d[a]-=1
        
for i in d:
    if d[i] !=0:
        print(i)