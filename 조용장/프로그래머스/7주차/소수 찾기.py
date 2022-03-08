from itertools import permutations
import math

# 소수인지 확인해야함
def check(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
    return True
                
def solution(numbers):
    answer = 0
    a=[]
    # numbers를 1자리수 부터 최대 자리수 까지 뽑아야함
    for k in range(1, len(numbers)+1):
        perlist = list(set(map(''.join, permutations(list(numbers), k))))
        # print(perlist)
        for i in perlist:
            if check(int(i)):
                a.append(int(i))
    answer=len(set(a))
    return answer