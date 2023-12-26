n,m = map(int,input().split())
d = dict()
for _ in range(n):
    site,id  = input().split()
    d[site] =id

for _  in range(m):
    s= input()
    print(d[s])