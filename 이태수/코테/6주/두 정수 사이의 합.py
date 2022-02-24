def solution(a, b):

    c = 0
    
    if(a>b):
        c=a
        a=b
        b=c
        
    answer=a
    while(a<b):
        a+=1
        answer+=a
        
    return answer

