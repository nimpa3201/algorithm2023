n = int(input())
arr =list(map(int,input().split()))
arr.sort()


if len(arr) %2 ==0:
    print(arr[0]*arr[-1])
else:
    print(arr[(n+1)//2-1]**2)