n,score, p = map(int,input().split())
if n ==0:
    print(1)
    exit()
    
arr =list(map(int,input().split()))


if min(arr) >= score and len(arr)+1 >=p:
    print(-1)
    exit()  

else:
    arr.append(score)
    arr.sort(reverse=True)
    tmp = arr[0]
    for i in range(1,len(arr)):
        
        cnt =1
   
        if tmp ==arr[i]:
            tmp =arr[i]
            if tmp == score:
                print(cnt)
                break
            
              
            
        else:
            cnt =i
            cnt+=1
            tmp =arr[i]
            if tmp == score:
               print(cnt)
               break
            
            
    
