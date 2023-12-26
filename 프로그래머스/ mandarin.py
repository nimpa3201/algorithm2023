def solution(k, tangerine):
    d = dict()
    select  = k
    cnt =0
    ans =0
    for i in tangerine:
        if i not in d:
            d[i] =1
        else:
            d[i]+=1
        
    sorted_dict = sorted(d.items() ,key =lambda item:-item[1] )
    print(sorted_dict)
    for x,y in sorted_dict:
        if cnt < select:
            cnt+=y
            ans +=1
        else:
            break
    return print(ans)
            
            
      





solution(6,[1, 3, 2, 5, 4, 5, 2, 3])	#3
solution(4,[1, 3, 2, 5, 4, 5, 2, 3])	#2
solution(2,[1, 1, 1, 1, 2, 2, 2, 3])	#1