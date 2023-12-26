n = int(input())
arr =[]
time=0
for _ in range(n):
    s,e =map(int,input().split())
    arr.append((s,e))
arr.sort(key =lambda x : (x[0],x[1]))
t = arr[0][0]+arr[0][1]
time +=t
for i in range(len(arr)-1):
    if t == arr[i+1][0]:
        time += arr[i+1][1]
    elif t > arr[i+1][0]:
        time +=arr[i+1][1]
        t = arr[i+1][0]+arr[i+1][1]
      
    else:
        time =arr[i+1][0]+arr[i+1][1]
        t = arr[i+1][0]+arr[i+1][1]
       

print(time)