n = int(input())
arr =[]
for _ in range(n):
    name,korean,english,math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    arr.append((name,korean,english,math))
    
arr.sort(key = lambda x : (-x[1],x[2],-x[3],x[0]))

for i in arr:
    print(i[0])