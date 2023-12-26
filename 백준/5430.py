from collections import deque
T = int(input())

for _ in range(T):
    cmd = input()
    n = int(input())
    arr=deque()
    arr = input()[1:-1].split(',')
    
    for i in cmd:
        if i =='R':
            arr = arr.reverse()
            
        if i =="D":
            arr.popleft()
    print(arr)
   