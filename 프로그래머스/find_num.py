def solution(numbers):
    ans =[]
    
    for i in range(len(numbers)):
        flag = True
        for j in range(i,len(numbers)):
         
            if numbers[i] <numbers[j]:
                ans.append(numbers[j])
                flag = False
                break
        if flag:
            ans.append(-1)
            flag=True
                
    
    return ans


solution([2, 3, 3, 5]) #[3, 5, 5, -1]
solution([9, 1, 5, 3, 6, 2])#[-1, 5, 6, 6, -1, -1]



def solution(numbers):
    stack = [0]
    ans = [-1] * len(numbers)  
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            ans[stack.pop()] = numbers[i]
        stack.append(i)
    
    return ans