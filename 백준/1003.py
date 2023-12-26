T = int(input())

for _ in range(T):
    num = int(input())
    arr0 = [0 for _ in range(40)]
    arr1 = [0 for _ in range(40)]
    
    arr0[0] =1
    arr0[1]=0
    arr1[0]=0
    arr1[1]=1
    
    for i in range(2,num+1):
        arr0[i] = arr0[i-1]+arr0[i-2]
        arr1[i] = arr1[i-1]+arr1[i-2]
    print(arr0[num],arr1[num])
    