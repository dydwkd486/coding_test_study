def solution(sizes):
    a=0
    b=0
    for i in sizes:
        a=max(a,max(i))
        b=max(b,min(i))
    print(a,b)
        
    answer =a*b
    return answer
