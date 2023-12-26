n = int(input())
arr = []
for _ in range(n):
    arr.append(input().split())

def strikes_funtion(number, guess):
    cnt = 0
    for i in range(3):
        if number[i] == guess[i]:
            cnt += 1
    return cnt

def ball_fuction(number, guess):
    cnt = 0
    for i in range(3):
        if guess[i] != number[i] and guess[i] in number:
            cnt += 1
    return cnt

def is_valid_guess(guess):
    return len(set(guess)) == 3

possible_answers = []
for number, strike, ball in arr:
    filter_answers = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                guess = str(i) + str(j) + str(k)
                if strikes_funtion(number, guess) == int(strike) and ball_fuction(number, guess) == int(ball) and  is_valid_guess(guess):
                    filter_answers.append(guess)
    possible_answers.append(filter_answers)

result = set(possible_answers[0])
for i in range(1, n):
    result = result.intersection(possible_answers[i])

print(len(result))




''''
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().split())
    
def strike_funtion(n, i, j, k):
    scnt = 0
    if n[0] == i:
        scnt += 1
    if n[1] == j:
        scnt += 1
    if n[2] == k:
        scnt += 1
    return scnt

def ball_funtion(n, i, j, k):
    bcnt = 0 
    if n[0] != i and (n[0] == j or n[0] == k):
        bcnt += 1
    if n[1] != j and (n[1] == i or n[1] == k):
        bcnt += 1
    if n[2] != k and (n[2] == j or n[2] == i):
        bcnt += 1
    return bcnt

possible_answers = []
for number, strike, ball in arr:
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                number_str = str(number)
                i_str = str(i)
                j_str = str(j)
                k_str = str(k)
                if ball_funtion(number_str, i_str, j_str, k_str) == int(ball) and strike_funtion(number_str, i_str, j_str, k_str) == int(strike):
                    possible_answers.append((i_str, j_str, k_str))

filtered_answers = []
for answer in possible_answers:
    is_valid = True
    for digit in answer:
        if answer.count(digit) > 1:
            is_valid = False
            break
    if is_valid:
        filtered_answers.append(answer)

print(len(filtered_answers))

'''


