n = int(input())
arr=[]
ans =0

for _ in range(n):
    arr.append(int(input()))
stack=[]



for i in range(n):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
  
    stack.append(arr[i])
    ans +=len(stack)-1
print(ans)


