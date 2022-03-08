def solution(n):
    answer = 0
    answer = format(655395, 'b')
    for i in range(655395+1, 1000001):
        print(i)
        if str(answer).count("1") == format(i, 'b').count("1"):
            print(i)
            return i