def solution(a, b):
    a,b=sorted([a,b])
    
    answer = 0
    
    for i in range(a,b+1,1):
        answer+=i
    
    return answer