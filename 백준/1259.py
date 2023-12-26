


def palindrome(s):
    if len(s)<=1:
        return 'yes'
    else:
        if s[0] ==s[-1]:
            return palindrome(s[1:-1])
        else:
            return 'no'



while True:
    n = input()
    if n =='0':
        break
    else:
        print(palindrome(n))

    