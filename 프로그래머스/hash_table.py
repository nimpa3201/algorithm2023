def solution(data, col, row_begin, row_end):
    data.sort(key= lambda x:(x[col-1],-x[0]))
    ans =0

    for i in range(row_begin-1,row_end):
        tmp =0
        for j in range(len(data[0])):
            tmp += data[i][j]%(i+1)       
        ans ^=tmp
    return ans
    
    
    
    
    






print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3))	#4