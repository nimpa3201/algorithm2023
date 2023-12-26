def solution(data, ext, val_ext, sort_by):
    ans = []
    index ={"code":0,"date":1,"maximun":2,"remain":3}
    #data.sort(key =lambda x : x[index[ext]])
    for i in data:
        if i[index[ext]] < val_ext:
           ans.append(i)
    ans.sort(key = lambda x : x[index[sort_by]] )    
    return ans
        
   





print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]	,"date"	,20300501,"remain"))

#[[3,20300401,10,8],[1,20300104,100,80]]