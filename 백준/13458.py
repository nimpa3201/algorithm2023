import math
n = int(input())
people = list(map(int,input().split()))
b,c = map(int,input().split())
cnt=0
for i in people:
    if i <=b :
        cnt+=1
    else:
        cnt +=1
        cnt +=math.ceil((i-b)/c)
print(cnt)
