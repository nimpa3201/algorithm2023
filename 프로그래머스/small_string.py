def solution(t, p):
    string = len(t)
    key =len(p)
    cnt=0
    for i in range(string-key+1):
        if int(p)>=int(t[i:i+key]):
            cnt+=1
    return cnt





solution("3141592","271")	#2
solution("500220839878","7")	#8
solution("10203","15")	#3