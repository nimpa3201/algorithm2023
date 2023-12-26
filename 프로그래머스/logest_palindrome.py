
def is_palindrome(x):
    if x == x[::-1]:
        return True


def solution(s):
    max=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if is_palindrome(s[i:j]):
                if max < len(s[i:j]):
                    max = len(s[i:j])
    return max

print(solution("abcdcba")) #7
print(solution("abacde")) #3