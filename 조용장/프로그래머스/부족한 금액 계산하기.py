# def solution(price, money, count):
#     answer = ((((1+count)*count)//2)*price)-money
#     if answer < 0:
#         answer=0

#     return answer

def solution(price, money, count):
    return max(0,((((1+count)*count)//2)*price)-money)