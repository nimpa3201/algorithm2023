import heapq
cnt=0
n = int(input())

arr =[]
for _ in range(n):
    arr.append(int(input()))
pq =[]    
tmp = arr[0] #  기호 1 번
def return_zero():
    return print(0)



if n ==1:
    return_zero()
    exit()

for i in range(1,n):
    heapq.heappush(pq,-arr[i])





max_person = -heapq.heappop(pq)
while tmp <=max_person:
 
    cnt+=1
    tmp+=1
    max_person-=1
    heapq.heappush(pq,-max_person)
    max_person = -heapq.heappop(pq)
    
   
    
    
print(cnt)