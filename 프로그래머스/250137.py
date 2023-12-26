def solution(bandage, health, attacks):
    cnt =0
    heal = health   
    for i in range(1,attacks[-1][0]+1):
        heal+=bandage[1]
        cnt+=1
        if heal > health :
            heal = health
        for time, damage in attacks:
            if i == time:
                cnt=0
                heal -= damage
                heal-=bandage[1]
        if cnt ==bandage[0]:
            heal+=bandage[2]
            cnt =0
        if heal+bandage[1] <=0:
            return -1         
    return heal+bandage[1]

print(solution([5, 1, 5],30,[[2, 10], [9, 15], [10, 5], [11, 5]])) #5
print(solution([3, 2, 7],20,[[1, 15], [5, 16], [8, 6]])) #-1
print(solution([4, 2, 7],20,[[1, 15], [5, 16], [8, 6]])) #-1
print(solution([1, 1, 1],5,[[1, 2], [3, 2]])) #3