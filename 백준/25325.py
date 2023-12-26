n = int(input())
arr = list((input().split()))
d = dict()
for i in arr:
    d[i] =0
for _ in range(n):
    name = list((input().split()))
    for i in name:
        if i in d:
            d[i]+=1
sorted_dict = sorted(d.items(), key = lambda item: (-item[1],item[0]))
for i in sorted_dict:
    print(*i)