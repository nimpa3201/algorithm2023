import math
import sys
x , y = map(int,input().split())
z = y*100//x
left = 1
right =1000000001
ans = sys.maxsize
while left <= right:
    mid = (left+right)//2

    if  ((y+mid)*100)//(x+mid) > z:
        right = mid-1
        ans = min(ans,mid)
    else:
        left = mid+1
print(ans if ans !=sys.maxsize else -1)