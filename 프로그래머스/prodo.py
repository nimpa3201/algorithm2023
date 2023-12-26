def solution(k, dungeons):
    cnt =0
    for i in range(len(dungeons)):
        dungeons[i].append(dungeons[i][0]-dungeons[i][1])
    dungeons.sort(key=lambda x:(-x[2],-x[0],-x[1]))
    for i in range(len(dungeons)):
        if k < dungeons[i][0]:
            break
            
        else:
            cnt+=1
            k = k-dungeons[i][1]
    return cnt




print(solution(80,[[80,20],[50,40],[30,10]]))	#3