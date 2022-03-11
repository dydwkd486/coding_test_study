def solution(brown, yellow):
    total = brown+yellow
    brown=brown//2
    answer=0
    for i in range(brown):
        # print((i+1)*(brown-i-1-2))
        if (i+1)*(brown-i-3)==yellow:
            answer=sorted([i+1+2,brown-i-1],reverse=True)
            break
        
    return answer