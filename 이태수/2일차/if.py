from datetime import datetime
people = 3
apple = 20


if people < apple / 5:
    print('신나는 사과 파티! 배 터지게 먹자!')

if apple % people > 0:
    print('사과가 맞지 않아 몇개는 쪼개 먹자!')

if people > apple:
    print('사람이 너무 많아 몇명은...')

if True:
    print('조건식 True')

if False:
    print('조건식 False')



hour = datetime.now().hour

if hour % 6 == 0:
    print('종이 울립니다.')
else:
    print('종이 울리지 않았습니다.')


if True:
    print('블럭에 속한 코드')

    if False:
        print('한 줄 더')

    if True:
        print('한 줄 더')

    print('블럭의 끝')

print('벌럭 끝')

if False:
    print('블럭에 속한 코드')

    if False:
        print('한 줄 더')

    if True:
        print('한 줄 더')

    print('블럭의 끝')

