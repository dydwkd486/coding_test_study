
SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼다'
DRAW = '비겼다'
LOSE = '졌다'

mine = '가위'
your = '바위'

if mine == your:
    result = DRAW
else:
    if mine == SCISSOR:
        if your == ROCK:
            result = LOSE
        else:
            result = WIN
    elif mine == ROCK:
        if your == SCISSOR:
            result = WIN
        else:
            result = LOSE
    elif mine == PAPER:
        if your == SCISSOR:
            result = LOSE
        else:
            result = WIN
    else:
        print('이상해요')

print(result)