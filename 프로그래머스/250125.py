def solution(board, h, w):
    global num
    num = len(board)
    cnt =0
    dxs = [1,-1,0,0]
    dys = [0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        if is_range(h+dx,w+dy):
            if board[h][w] == board[h+dx][w+dy]:
                cnt+=1
    return cnt
def is_range(x,y):
    return 0<=x<num and 0<=y<num

print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]],1,1)) #2