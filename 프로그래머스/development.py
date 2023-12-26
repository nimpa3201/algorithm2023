def solution(progresses, speeds):
    ans =[]
    tmp =0
    result=[]
    for i in range(len(progresses)):
        cnt=0
        while progresses[i]<100:
            progresses[i]+=speeds[i]
            cnt+=1

        ans.append(cnt)
        tmp =ans[0]
        count=0
        for i in range(1,len(ans)):    # 날짜는 나왔는데 어떻게 묶어야 랄 지 모르갰다,,
            if tmp <=ans[i]:
                tmp= ans[i]
                count+=1
                result.append(count)
            else:
                count+=1
                    
                
    return print(result),print(ans)

solution([93, 30, 55],[1, 30, 5])	#[2, 1]
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])	#[1, 3, 2]