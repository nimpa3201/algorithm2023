h,w = map(int,input().split())
arr = list(map(int,input().split()))
matrix = [[0 for _ in range(w)] for _ in range(h)]
cnt =0
tmp =0

for i in range(w):
    for j in range(arr[i]):
            matrix[j][i] = 'x'

print(matrix)
for i in range(h):
    flag = False
    tmp=0
    for j in range(w):
        if matrix[i][j] == 'x':
            flag= True
           
      
            #print(i,j)
           
            
        else:
            flag= False
            tmp +=1
        if flag :#and matrix[i][j-1]!='x':
            print(tmp,i,j)
            cnt+=tmp
            
         
print(cnt)
print(tmp)
            
            
        
        