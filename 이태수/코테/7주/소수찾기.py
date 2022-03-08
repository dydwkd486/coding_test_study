from itertools import permutations
def is_prime_number(x):
    if x == 1:
        return False 
    if x == 0:
        return False 
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(numbers):
    a=len(numbers)
    b=[]
    c=[]
    d=[]
    answer = 0
    while(a>0):
        b=list(permutations(numbers,a))
        c=list(set(map(''.join, b)))
        
        for i in set(c):
            if is_prime_number(int(i)):
                d.append(int(i))
        a-=1
    print(set(d))
    answer = len(set(d))
    
    
    return answer