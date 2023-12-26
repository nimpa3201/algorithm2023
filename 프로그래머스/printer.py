def solution(priorities, location):
    cnt=0
    target =priorities[location]
    for i in priorities:
        if i == max(priorities):
            priorities.pop(0)
            cnt+=1
            if i == target:
                print(cnt)
        else:
            priorities.append(priorities.pop(0))
            
    
    









solution([2, 1, 3, 2],2)	#1
solution([1, 1, 9, 1, 1, 1]	,0)	#5
