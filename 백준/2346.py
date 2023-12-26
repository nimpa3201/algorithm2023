from collections import deque
n = int(input())
step = list(map(int,input().split()))
number = deque()
for i in range(1,n+1):
    number.append(i)
print(1,end=' ')
t=step[0]
number.popleft()
while number:

  
    if t >0  and number:
        for i in range(t-1):
            number.append(number.popleft())
        
        a= number.popleft()
      
        print(a,end=' ')
        t =step[a-1]
      
        
    if t<0 and number:
        for i in range(-t):
            
            #print(number)
            number.appendleft(number.pop())
          
        a =number.popleft()
        print(a,end=' ')
        t=step[a-1]
        #print(t)