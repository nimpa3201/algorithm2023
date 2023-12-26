import sys
def solution(brown, yellow):
    ans = sys.maxsize
    s =set()
    t = brown+yellow
    li=[]
    for i in range(1,t//2):
        if t%i ==0:
            s.add((t//i,i))
    for j in s:
        if j[0]-j[1]<ans:
            ans =abs(j[0]-j[1])
            li.append([j[0],j[1]])
    li[-1].sort(reverse = True)
    return li[-1]
print(solution(24,24))