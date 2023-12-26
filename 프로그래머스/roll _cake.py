from collections import deque

def solution(topping):
    a = set()
    b = set()
    cnt =0
    q = deque(topping)
    A = len(q)
    while q:
        if A%2 ==0:
            a.add(q[0])
            b.add(q[-1])
            q.popleft()
            q.pop()
    
        print(a,b)
        
        if A%2 ==1 :
            a.add(q[0])
            b.add(q[-1])
            q.popleft()
            if len(q)==1:
                a.add(q.pop())
                continue
            q.pop() 
  
        if len(a) == len(b):
            cnt+=1
    
        # if len(a)>len(topping1):
        #     break
    return cnt


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))	#2
print(solution([1, 2, 3, 1, 4]))	#0