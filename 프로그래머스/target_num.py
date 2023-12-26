def solution(numbers, target):
    bin= [0]
    for i in numbers:
        ans = []
        for j in bin : 
            ans.append(j+i)
            ans.append(j-i)
        bin = ans
    return bin.count(target)    
        
print( solution([1, 1, 1, 1, 1],3))