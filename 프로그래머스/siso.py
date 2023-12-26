def solution(weights):
    cnt=0
    for i in range( len(weights)):
        for j in range(len(weights)):
            if i == j :
                continue
            else:
                if weights[i] ==weights[j] :
                    cnt+=1
                    weights[i]=0
                    weights[j]=0
    print(weights)   

    
    arr =[[] for i in range(len(weights))]
    for i in range(len(weights)):
        for j in range(2,5):
            arr[i].append(weights[i]*j)
    print(arr)
 
    for i in range(len(weights)):
        for j in range(3):
            for k in range(len(weights)):
                for o in range(3):
            
                    if i == k :
                        continue
                    else:
                        tmp =arr[i][j]
                        #print(i,j)
                        #print(k,j)
                        #print(arr[i][j],arr[k][o])
                        if tmp == arr[k][o] and tmp * arr[k][o]!=0:
                            print(arr[k][o],tmp)
                            #print(tmp)
                            
                            cnt+=1
                            break
                            
                        
    return cnt//2
                    
    
    






print(solution([100,180,360,100,270])) #4

# 234