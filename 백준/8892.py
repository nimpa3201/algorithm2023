def is_palindrome(s):
    if len(s)<= 1:
        return True
    else:
        if s[0] ==s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False





t = int(input())
for _ in range(t):
    arr= []
    ans =[]
    k = int(input())
    for _ in range(k):
        arr.append(input())
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):  
            s= ''
            t= ''
            s+=arr[i]+arr[j]
            t += arr[j]+arr[i]
            if is_palindrome(s):
                ans.append(s)
            if is_palindrome(t):
                ans.append(t)
    print(ans[0] if len(ans) !=0 else 0)


  