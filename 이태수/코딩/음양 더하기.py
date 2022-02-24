def solution(absolutes, signs):

    answer=0
    for i,v in enumerate(absolutes):
        if(not(signs[i])):
            v*=-1
        answer+=v
     
    return answer