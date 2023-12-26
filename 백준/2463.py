n = int(input())
matrix = [[0 for _ in range(100)] for _ in range(100)]
ans =0
for _ in range(n):
    x,y = map(int,input().split())
    
    for i in range(10):
        for j in range(10):
            matrix[x-1+i][y-1+j] =1
        


for i in matrix:
    ans += sum(i)
print(ans)