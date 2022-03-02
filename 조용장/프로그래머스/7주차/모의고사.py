def solution(answers):
    # print(len(answers*2000))
    answer = []
    answers=answers
    supoja_1=[1,2,3,4,5]*2000
    supoja_2=[2,1,2,3,2,4,2,5]*1250
    supoja_3=[3,3,1,1,2,2,4,4,5,5]*1000
    count=[0,0,0]
    
    for i in range(len(answers)):
        if answers[i]==supoja_1[i]:
            count[0]+=1
        if answers[i]==supoja_2[i]:
            count[1]+=1
        if answers[i]==supoja_3[i]:
            count[2]+=1

    # print(max(count))
    for i in range(len(count)):
        if count[i]==(max(count)):
            answer.append(i+1)
        
    
    return answer