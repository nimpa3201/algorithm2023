n,m = map(int,input().split())
d =dict()
for _ in range(n):
  
    word = input()
    if len(word) >= m:
        if word in d:
            d[word]+=1
        else:
            d[word]=1

sorted_dict = sorted(d.items(),key =lambda x: (-x[1],-len(x[0]),x[0]))

for i,_ in sorted_dict:
    print(i)