n,k = map(int,input().split())
num =1
ans =0
divide =1
for i in range(n,n-k,-1):
    num =num*i
for i in range(1,k+1):
    divide = divide*i   
ans = num//divide
print(ans%10007)