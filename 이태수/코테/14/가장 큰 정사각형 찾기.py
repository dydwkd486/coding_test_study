
def solution(board):
    answer = 0
    for i, v in enumerate(board):
        for j, v2 in enumerate(v):
             if board[i][j] != 0 and i != 0  and j !=0:
                    board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1]) + 1
        if answer < max(board[i]):
            answer = max(board[i])
    return answer ** 2