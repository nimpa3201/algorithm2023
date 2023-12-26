n = int(input())
arr =list(map(int,input().split()))
arr.sort(reverse=True)
big = arr[:n//2]
small = arr[n//2:]
print(small)
print(big)

for i in range(1,n):
    if i % 2==1:
        small.insert(i,big[i-1])
        if i-1 >=2:
            break
    else:
        small.insert(i+1,big[i+1])
        
print(small)