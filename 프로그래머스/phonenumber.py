def solution(phone_book):
    phone_book.sort(key=len)
    s= set()
    for i in phone_book:
        s.add(i)
        for j in i:
            
        
    
    return phone_book


print(solution(["119", "97674223", "1195524421"]))	#false
solution(["123","456","789"])	#true
print(solution(["12","123","1235","567","88"]))	#false